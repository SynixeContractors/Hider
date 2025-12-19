#include "script_component.hpp"

class CfgPatches {
    class ADDON {
        name = QUOTE(COMPONENT);
        units[] = {};
        weapons[] = {};
        requiredVersion = REQUIRED_VERSION;
        requiredAddons[] = {
            "cba_main",
            "A3_Armor_F_Beta_APC_Tracked_01",
        };
        skipWhenMissingDependencies = 1;
        author = "Synixe Contractors";
        VERSION_CONFIG;
    };
};

#include "CfgEventHandlers.hpp"
