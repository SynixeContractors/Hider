def get_addon(source):
    # Assume any CBA changes are to vanilla
    bi = ["cba_", "A3_Air_F", "A3_Characters_F", "A3_Opf", "A3_OpF", "A3_Soft_", "A3_Armor_", "A3_expEden", "A3_Structures_F", "A3_Modules_F", "A3_Drones_F", "A3_Missions_F", "A3_Boat_F", "A3_Static_F", "A3_Supplies_F", "A3_Weapons_F", "A3_Data_F", "Air_Globe", "Armor_Globe", "Soft_Globe", "Weapons_Globe"]
    if source.startswith("ace_"):
        return "ace"
    elif source.startswith("RF_"):
        return "rf"
    elif source.startswith("WS_") or "lxWS" in source:
        return "ws"
    elif source.startswith("MU_") or source == "<null>":
        # MU has a broken unit
        return "mu"
    elif source.startswith("Atlas_") or source.startswith("A3_Atlas_") or source.startswith("A3_Characters_expEden"):
        return "atlas"
    elif source.startswith("Aegis_") or source.startswith("A3_Aegis_"):
        return "aegis"
    elif source.startswith("tacs_"):
        return "tacs"
    elif source.startswith("HSim"):
        return "toh"
    elif source.startswith("vtf_kf"):
        return "korsac"
    elif source == "MELB":
        return "melb"
    elif any(source.startswith(prefix) for prefix in bi):
        return "bi"
    else:
        print(f"Unknown source addon: {source}")
        return ""

units = []
with open("units.txt") as f:
    for line in f:
        if line.startswith("$"):
            continue
        else:
            # units;parent;source
            parts = line.strip().split(";")
            if len(parts) >= 3:
                unit = parts[0]
                parent = parts[1]
                source = parts[2]
                # defining this breaks the class
                if unit == "Helicopter_Base_F":
                    continue
                units.append({
                    "unit": unit,
                    "parent": parent,
                    "source": source
                })

units_dict = {unit["unit"]: unit["parent"] for unit in units}
sorted_units = []
while units_dict:
    for unit, parent in list(units_dict.items()):
        if parent not in units_dict:
            if "Module" in unit:
                # skip modules, we don't want to hide them
                del units_dict[unit]
                continue
            sorted_units.append({
                "unit": unit,
                "parent": parent,
                "source": next(u["source"] for u in units if u["unit"] == unit)
            })
            del units_dict[unit]
units = sorted_units

print(f"Parsed {len(units)} units.")

addons = {}
for unit_info in units:
    unit = unit_info["unit"]
    parent = unit_info["parent"]
    source = unit_info["source"]
    addon = get_addon(source)
    if addon == "":
        continue
    if addon not in addons:
        addons[addon] = {}
    addons[addon].setdefault("units", []).append((unit, parent, source))

side = None
with open("groups.txt") as f:
    for line in f:
        if line.startswith("$"):
            side = line[1:].strip()
        else:
            # group;parent;source
            parts = line.strip().split(";")
            if len(parts) >= 3:
                group = parts[0]
                sources = parts[1]
                sources = sources.strip("[]").split(",")
                for source in sources:
                    source = source.strip().strip('"')
                    addon = get_addon(source)
                    if addon == "":
                        continue
                    if addon not in addons:
                        addons[addon] = {}
                    if "groups" not in addons[addon]:
                        addons[addon]["groups"] = []
                    if not any(g["group"] == group for g in addons[addon]["groups"]):
                        addons[addon]["groups"].append({
                            "group": group,
                            "source": source,
                            "side": side
                        })

for addon, data in addons.items():
    units = data["units"]
    groups = data.get("groups", [])
    print(f"Addon {addon} has {len(units)} units.")
    all_parents = set(member[1] for member in units)
    defined_classnames = set(member[0] for member in units)
    undefined_parents = all_parents - defined_classnames
    undefined_parents = sorted(undefined_parents)
    unique_sources = set()
    for member in units:
        if member[2] != "<null>":
            unique_sources.add(member[2])
    for group in groups:
        if group["source"] != "<null>":
            unique_sources.add(group["source"])
    dir = f"addons/{addon}"
    # create dir if not exists
    import os
    os.makedirs(dir, exist_ok=True)
    with open(f"{dir}/CfgVehicles.hpp", "w") as f:
        f.write("// Auto-generated file. Do not edit.\n\n")
        f.write("class CfgVehicles {\n")
        for external in undefined_parents:
            f.write(f"class {external};\n")
        f.write("\n")
        for unit, parent, source in units:
            f.write(f"class {unit}: {parent} {{ scope = 1; scopeCurator = 1; }};\n")
        f.write("};\n")
    with open(f"{dir}/config.cpp", "w") as f:
        f.write("""#include "script_component.hpp"
class CfgPatches {{
    class ADDON {{
        name = QUOTE(COMPONENT);
        units[] = {{}};
        weapons[] = {{}};
        requiredVersion = REQUIRED_VERSION;
        requiredAddons[] = {{
            "synixe_hider_main",
{}
        }};
        skipWhenMissingDependencies = 1;
        author = "Synixe Contractors";
        addonRootClass = "A3_Data_F";
        VERSION_CONFIG;
    }};
}};
#include "CfgVehicles.hpp"
""".format(",\n".join(f'"{s}"' for s in unique_sources)))
    with open(f"{dir}/$PBOPREFIX$", "w") as f:
        f.write(f"s\\synixe_hider\\addons\\{addon}\n")
    with open(f"{dir}/script_component.hpp", "w") as f:
        f.write(f'#define COMPONENT {addon}\n')
        f.write('#include "..\\main\\script_mod.hpp"\n')
        f.write('#include "..\\main\\script_macros.hpp"\n')

    if not groups or len(groups) == 0:
        continue
    sides = {}
    for group in groups:
        sides.setdefault(group["side"], []).append(group)
    with open(f"{dir}/CfgGroups.hpp", "w") as f:
        f.write("// Auto-generated file. Do not edit.\n\n")
        f.write("class CfgGroups {\n")
        for side, groups in sides.items():
            f.write(f"    class {side} {{\n")
            for group_info in groups:
                group = group_info["group"]
                f.write(f"        delete {group};\n")
            f.write("    };\n")
        f.write("};\n")
    with open(f"{dir}/config.cpp", "a") as f:
        f.write('#include "CfgGroups.hpp"\n')
