#include "script_component.hpp"
class CfgPatches {
    class ADDON {
        name = QUOTE(COMPONENT);
        units[] = {};
        weapons[] = {};
        requiredVersion = REQUIRED_VERSION;
        requiredAddons[] = {
            "synixe_hider_main",
"Vehicles_F_lxWS_APC_Wheeled_01",
"Air_1_F_lxWS",
"Vehicles_F_lxWS_Offroad_01",
"Air_F_lxWS_Heli_Light_02",
"characters_1_F_lxWS",
"data_f_lxWS_rf_compatibility",
"Air_F_lxWS",
"A3_Aegis_Air_F_Aegis_UAV_02_lxWS",
"Characters_1_f_lxWS_uniform",
"vehicles_1_F_lxWS_APC_Wheeled_02",
"vehicles_1_F_lxWS_APC_Tracked_02",
"Vehicles_F_lxWS_zu23",
"A3_Atlas_Air_F_Atlas_UAV_02_lxWS",
"Vehicles_F_lxWS",
"Vehicles_F_lxWS_Truck_02",
"A3_Opf_Air_F_Opf_UAV_02_lxWS",
"Characters_f_lxWS"
        };
        skipWhenMissingDependencies = 1;
        author = "Synixe Contractors";
        addonRootClass = "A3_Data_F";
        VERSION_CONFIG;
    };
};
#include "CfgVehicles.hpp"
#include "CfgGroups.hpp"
