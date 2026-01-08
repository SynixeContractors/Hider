#include "script_component.hpp"
class CfgPatches {
    class ADDON {
        name = QUOTE(COMPONENT);
        units[] = {};
        weapons[] = {};
        requiredVersion = REQUIRED_VERSION;
        requiredAddons[] = {
            "synixe_hider_main",
"MU_LIV",
"MU_asset",
"MU_mercs",
"MU_MILITIA",
"MU_islam",
"MU_doc_diver",
"MU_greendagers",
"MU_vehicles",
"MU_RU",
"MU_civilian",
"MU_divers",
"MU_SF",
"MU_CTRG"
        };
        skipWhenMissingDependencies = 1;
        author = "Synixe Contractors";
        addonRootClass = "A3_Data_F";
        VERSION_CONFIG;
    };
};
#include "CfgVehicles.hpp"
#include "CfgGroups.hpp"
