| *** Settings *** |
| Library | C:\\Users\\i067382\\PycharmProjects\\eztestRobot\\OSHelper.py |

| *** Test Cases *** |
| tcase01 |
|  | [Documentation] | hive_query03 SUM and GROUP BY
|  | ${result} = | Shell Command | echo hello | True
|  | Should Contain | ${result} | hello
