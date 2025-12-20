#include "script_component.hpp"
class CfgPatches {
    class ADDON {
        name = QUOTE(COMPONENT);
        units[] = {};
        weapons[] = {};
        requiredVersion = REQUIRED_VERSION;
        requiredAddons[] = {
            "synixe_hider_main",
"MU_divers",
"MU_CTRG",
"MU_greendagers",
"MU_LIV",
"MU_civilian",
"MU_RU",
"MU_mercs",
"MU_doc_diver",
"MU_asset",
"MU_MILITIA",
"MU_islam",
"MU_vehicles",
"MU_SF"
        };
        skipWhenMissingDependencies = 1;
        author = "Synixe Contractors";
        addonRootClass = "A3_Data_F";
        VERSION_CONFIG;
    };
};
#include "CfgVehicles.hpp"
#include "CfgGroups.hpp"
