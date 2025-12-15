#include "..\script_component.hpp"

GVAR(sides) = [0,1,2,3];

private _factions = QUOTE(getNumber (_x >> ""side"") in GVAR(sides)) configClasses (configFile >> "CfgFactionClasses");

{
    GVAR(faction) = configName _x;
    private _units = QUOTE(getText (_x >> ""faction"") == GVAR(faction)) configClasses (configFile >> "CfgVehicles");
    _units = _units select { 
        private _sim = getText (_x >> "simulation");
        _sim != "house" && _sim != "thingX" && _sim != "parachute"
    };

    "ace" callExtension ["clipboard:append", [format ["$%1%2", GVAR(faction), endl]]];

    {
        private _parent = configName inheritsFrom _x;
        private _source = (configSourceAddonList _x) select 0;
        "ace" callExtension ["clipboard:append", [format ["%1;%2;%3;%4", configName _x, _parent, _source, endl]]];
    } forEach _units;

} forEach _factions;
"ace" callExtension ["clipboard:complete", []];
