#include "..\script_component.hpp"

{
    "ace" callExtension ["clipboard:append", [format ["$%1%2", _x, endl]]];
    private _groups = "true" configClasses (configFile >> "CfgGroups" >> _x);
    {
        private _source = (configSourceAddonList _x);
        "ace" callExtension ["clipboard:append", [format ["%1;%2;%3", configName _x, _source, endl]]];
    } forEach _groups;
} forEach ["West", "East", "Indep"];
"ace" callExtension ["clipboard:complete", []];
