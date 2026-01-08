#include "script_component.hpp"
class CfgPatches {
    class ADDON {
        name = QUOTE(COMPONENT);
        units[] = {};
        weapons[] = {};
        requiredVersion = REQUIRED_VERSION;
        requiredAddons[] = {
            "synixe_hider_main",
"RF_Air_heli_medium_ec",
"RF_Characters_Backpack",
"RF_Vehicles_Pickup_01",
"RF_Vehicles_Truck_03",
"RF_Characters_Uniform",
"RF_Vehicles_TwinMortar",
"RF_Vehicles_Truck_01",
"RF_Air_RC40",
"RF_Vehicles_CommandoMortar",
"RF_Air_Heli_Light_03",
"RF_Characters",
"RF_Data_ws_compatibility"
        };
        skipWhenMissingDependencies = 1;
        author = "Synixe Contractors";
        addonRootClass = "A3_Data_F";
        VERSION_CONFIG;
    };
};
#include "CfgVehicles.hpp"
#include "CfgGroups.hpp"
