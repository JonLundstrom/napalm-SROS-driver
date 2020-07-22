## **Testing for NAPALM with Nokia SR OS**
1) To run the test framework, first install pytest: ```pip install pytest```
2) Locate the file: \"test/unit/sros/TestDriver.py\"
3) Run \"Class TestConfigNokiaSROSDriver\" to test all the config methods of NAPALM
    + Location of files required by this test:
        - `napalm_sros/templates/set_hostname.j2`
        - `test/unit/sros/initial.conf` - Initial configuration sample
        - `test/unit/sros/merge_good.conf` - Merge config example
        - `test/unit/sros/merge_good.diff` - Compare output for merge
        - `test/unit/sros/merge_typo.conf` - Merege config example with error
        - `test/unit/sros/new_good.conf` - Replace config example
        - `test/unit/sros/new_good.diff` - Compare output for replace
        - `test/unit/sros/new_typo.conf` - Replace config example with err
5) Run `Class TestGetterNokiaSROSDriver` to test all the getter methods of NAPALM
6) Location of mock files used for these tests is : `test/unit/sros/mock_data`

We welcome suggestions and contributions of additional tests for the framework. Please contact the Nokia owners of this repository for how to contribute.
