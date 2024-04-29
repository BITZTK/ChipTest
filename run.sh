#!/bin/bash

config_file="./config.ini"
#export CONFIG_FILE=$(realpath $config_file)

READ_CONFIG() {
  code="import configparser; \
        cfg = configparser.ConfigParser(); \
        cfg.read('$config_file'); \
        value = cfg.get('GLOBAL_INFO', '$1'); \
        print(value)
       "
  value=$(python3 -c "$code")
  echo "$value"
}

dump_enable=$(READ_CONFIG "dump_enable")
dump_type=$(READ_CONFIG "dump_type")
dump_file=$(READ_CONFIG "dump_file")
dump_start_cycle=$(READ_CONFIG "dump_start_cycle")

DUMP_INFO="dump_enable=$dump_enable dump_type=$dump_type dump_file=$dump_file dump_start_cycle=$dump_start_cycle"

echo "$DUMP_INFO"


COCOTB_RESOLVE_X=ZEROS make -j 128 | tee test_log.log


