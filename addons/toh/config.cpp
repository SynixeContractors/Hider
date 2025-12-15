#include "script_component.hpp"
class CfgPatches {
    class ADDON {
        name = QUOTE(COMPONENT);
        units[] = {};
        weapons[] = {};
        requiredVersion = REQUIRED_VERSION;
        requiredAddons[] = {
            "synixe_hider_main",
"HSim_Characters_History_H",
"HSim_Characters_Woman_H_Uniforms"
        };
        skipWhenMissingDependencies = 1;
        author = "Synixe Contractors";
        addonRootClass = "A3_Data_F";
        VERSION_CONFIG;
    };
};
#include "CfgVehicles.hpp"
