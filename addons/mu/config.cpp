#include "script_component.hpp"
class CfgPatches {
    class ADDON {
        name = QUOTE(COMPONENT);
        units[] = {};
        weapons[] = {};
        requiredVersion = REQUIRED_VERSION;
        requiredAddons[] = {
            "synixe_hider_main",
"MU_CTRG",
"MU_LIV",
"MU_MILITIA",
"MU_RU",
"MU_SF",
"MU_asset",
"MU_civilian",
"MU_divers",
"MU_doc_diver",
"MU_greendagers",
"MU_islam",
"MU_mercs",
"MU_vehicles"
        };
        skipWhenMissingDependencies = 1;
        author = "Synixe Contractors";
        addonRootClass = "A3_Data_F";
        VERSION_CONFIG;
    };
};
#include "CfgVehicles.hpp"
#include "CfgGroups.hpp"
