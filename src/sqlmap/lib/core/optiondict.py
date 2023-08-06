#!/usr/bin/env python
"""Copyright (c) 2006-2023 sqlmap developers (https://sqlmap.org/) See the file
'LICENSE' for copying permission."""

optDict = {
    # Family: {"parameter name": "parameter datatype"},
    # --OR--
    # Family: {"parameter name": ("parameter datatype", "category name used for common outputs feature")},
    "Target": {
        "direct": "string",
        "url": "string",
        "logFile": "string",
        "bulkFile": "string",
        "requestFile": "string",
        "sessionFile": "string",
        "googleDork": "string",
        "configFile": "string",
    },
    "Request": {
        "method": "string",
        "data": "string",
        "paramDel": "string",
        "cookie": "string",
        "cookieDel": "string",
        "liveCookies": "string",
        "loadCookies": "string",
        "dropSetCookie": "boolean",
        "agent": "string",
        "mobile": "boolean",
        "randomAgent": "boolean",
        "host": "string",
        "referer": "string",
        "headers": "string",
        "authType": "string",
        "authCred": "string",
        "authFile": "string",
        "abortCode": "string",
        "ignoreCode": "string",
        "ignoreProxy": "boolean",
        "ignoreRedirects": "boolean",
        "ignoreTimeouts": "boolean",
        "proxy": "string",
        "proxyCred": "string",
        "proxyFile": "string",
        "proxyFreq": "integer",
        "tor": "boolean",
        "torPort": "integer",
        "torType": "string",
        "checkTor": "boolean",
        "delay": "float",
        "timeout": "float",
        "retries": "integer",
        "retryOn": "string",
        "rParam": "string",
        "safeUrl": "string",
        "safePost": "string",
        "safeReqFile": "string",
        "safeFreq": "integer",
        "skipUrlEncode": "boolean",
        "csrfToken": "string",
        "csrfUrl": "string",
        "csrfMethod": "string",
        "csrfData": "string",
        "csrfRetries": "integer",
        "forceSSL": "boolean",
        "chunked": "boolean",
        "hpp": "boolean",
        "evalCode": "string",
    },
    "Optimization": {
        "optimize": "boolean",
        "predictOutput": "boolean",
        "keepAlive": "boolean",
        "nullConnection": "boolean",
        "threads": "integer",
    },
    "Injection": {
        "testParameter": "string",
        "skip": "string",
        "skipStatic": "boolean",
        "paramExclude": "string",
        "paramFilter": "string",
        "dbms": "string",
        "dbmsCred": "string",
        "os": "string",
        "invalidBignum": "boolean",
        "invalidLogical": "boolean",
        "invalidString": "boolean",
        "noCast": "boolean",
        "noEscape": "boolean",
        "prefix": "string",
        "suffix": "string",
        "tamper": "string",
    },
    "Detection": {
        "level": "integer",
        "risk": "integer",
        "string": "string",
        "notString": "string",
        "regexp": "string",
        "code": "integer",
        "smart": "boolean",
        "textOnly": "boolean",
        "titles": "boolean",
    },
    "Techniques": {
        "technique": "string",
        "timeSec": "integer",
        "uCols": "string",
        "uChar": "string",
        "uFrom": "string",
        "dnsDomain": "string",
        "secondUrl": "string",
        "secondReq": "string",
    },
    "Fingerprint": {
        "extensiveFp": "boolean",
    },
    "Enumeration": {
        "getAll": "boolean",
        "getBanner": ("boolean", "Banners"),
        "getCurrentUser": ("boolean", "Users"),
        "getCurrentDb": ("boolean", "Databases"),
        "getHostname": "boolean",
        "isDba": "boolean",
        "getUsers": ("boolean", "Users"),
        "getPasswordHashes": ("boolean", "Passwords"),
        "getPrivileges": ("boolean", "Privileges"),
        "getRoles": ("boolean", "Roles"),
        "getDbs": ("boolean", "Databases"),
        "getTables": ("boolean", "Tables"),
        "getColumns": ("boolean", "Columns"),
        "getSchema": "boolean",
        "getCount": "boolean",
        "dumpTable": "boolean",
        "dumpAll": "boolean",
        "search": "boolean",
        "getComments": "boolean",
        "getStatements": "boolean",
        "db": "string",
        "tbl": "string",
        "col": "string",
        "exclude": "string",
        "pivotColumn": "string",
        "dumpWhere": "string",
        "user": "string",
        "excludeSysDbs": "boolean",
        "limitStart": "integer",
        "limitStop": "integer",
        "firstChar": "integer",
        "lastChar": "integer",
        "sqlQuery": "string",
        "sqlShell": "boolean",
        "sqlFile": "string",
    },
    "Brute": {
        "commonTables": "boolean",
        "commonColumns": "boolean",
        "commonFiles": "boolean",
    },
    "User-defined function": {
        "udfInject": "boolean",
        "shLib": "string",
    },
    "File system": {
        "fileRead": "string",
        "fileWrite": "string",
        "fileDest": "string",
    },
    "Takeover": {
        "osCmd": "string",
        "osShell": "boolean",
        "osPwn": "boolean",
        "osSmb": "boolean",
        "osBof": "boolean",
        "privEsc": "boolean",
        "msfPath": "string",
        "tmpPath": "string",
    },
    "Windows": {
        "regRead": "boolean",
        "regAdd": "boolean",
        "regDel": "boolean",
        "regKey": "string",
        "regVal": "string",
        "regData": "string",
        "regType": "string",
    },
    "General": {
        "trafficFile": "string",
        "abortOnEmpty": "boolean",
        "answers": "string",
        "batch": "boolean",
        "base64Parameter": "string",
        "base64Safe": "boolean",
        "binaryFields": "string",
        "charset": "string",
        "checkInternet": "boolean",
        "cleanup": "boolean",
        "crawlDepth": "integer",
        "crawlExclude": "string",
        "csvDel": "string",
        "dumpFile": "string",
        "dumpFormat": "string",
        "encoding": "string",
        "eta": "boolean",
        "flushSession": "boolean",
        "forms": "boolean",
        "freshQueries": "boolean",
        "googlePage": "integer",
        "harFile": "string",
        "hexConvert": "boolean",
        "outputDir": "string",
        "parseErrors": "boolean",
        "postprocess": "string",
        "preprocess": "string",
        "repair": "boolean",
        "saveConfig": "string",
        "scope": "string",
        "skipHeuristics": "boolean",
        "skipWaf": "boolean",
        "testFilter": "string",
        "testSkip": "string",
        "webRoot": "string",
    },
    "Miscellaneous": {
        "alert": "string",
        "beep": "boolean",
        "dependencies": "boolean",
        "disableColoring": "boolean",
        "listTampers": "boolean",
        "noLogging": "boolean",
        "offline": "boolean",
        "purge": "boolean",
        "resultsFile": "string",
        "tmpDir": "string",
        "unstable": "boolean",
        "updateAll": "boolean",
        "wizard": "boolean",
        "verbose": "integer",
    },
    "Hidden": {
        "dummy": "boolean",
        "disablePrecon": "boolean",
        "profile": "boolean",
        "forceDns": "boolean",
        "murphyRate": "integer",
        "smokeTest": "boolean",
    },
    "API": {
        "api": "boolean",
        "taskid": "string",
        "database": "string",
    },
}
