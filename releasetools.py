# Copyright (C) 2020 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import common

# Firmware - sagit-firmware
def FullOTA_InstallEnd(info):
    common.ZipWriteStr(info.output_zip, "firmware-update/abl.elf", "device/xiaomi/sagit-firmware/firmware-update/abl.elf")
    common.ZipWriteStr(info.output_zip, "firmware-update/BTFM.bin", "device/xiaomi/sagit-firmware/firmware-update/BTFM.bin")
    common.ZipWriteStr(info.output_zip, "firmware-update/cmnlib64.mbn", "device/xiaomi/sagit-firmware/firmware-update/cmnlib64.mbn")
    common.ZipWriteStr(info.output_zip, "firmware-update/cmnlib.mbn", "device/xiaomi/sagit-firmware/firmware-update/cmnlib.mbn")
    common.ZipWriteStr(info.output_zip, "firmware-update/devcfg.mbn", "device/xiaomi/sagit-firmware/firmware-update/devcfg.mbn")
    common.ZipWriteStr(info.output_zip, "firmware-update/hyp.mbn", "device/xiaomi/sagit-firmware/firmware-update/hyp.mbn")
    common.ZipWriteStr(info.output_zip, "firmware-update/keymaster.mbn", "device/xiaomi/sagit-firmware/firmware-update/keymaster.mbn")
    common.ZipWriteStr(info.output_zip, "firmware-update/logfs_ufs_8mb.bin", "device/xiaomi/sagit-firmware/firmware-update/logfs_ufs_8mb.bin")
    common.ZipWriteStr(info.output_zip, "firmware-update/NON-HLOS.bin", "device/xiaomi/sagit-firmware/firmware-update/NON-HLOS.bin")
    common.ZipWriteStr(info.output_zip, "firmware-update/rpm.mbn", "device/xiaomi/sagit-firmware/firmware-update/rpm.mbn")
    common.ZipWriteStr(info.output_zip, "firmware-update/storsec.mbn", "device/xiaomi/sagit-firmware/firmware-update/storsec.mbn")
    common.ZipWriteStr(info.output_zip, "firmware-update/tz.mbn", "device/xiaomi/sagit-firmware/firmware-update/tz.mbn")
    common.ZipWriteStr(info.output_zip, "firmware-update/xbl.elf", "device/xiaomi/sagit-firmware/firmware-update/xbl.elf")

# Write Firmware updater-script
    info.script.AppendExtra('')
    info.script.AppendExtra('# ---- radio update tasks ----')
    info.script.AppendExtra('')
    info.script.AppendExtra('ui_print("Patching firmware images...");')
    info.script.AppendExtra('package_extract_file("firmware-update/cmnlib64.mbn", "/dev/block/bootdevice/by-name/cmnlib64");')
    info.script.AppendExtra('package_extract_file("firmware-update/NON-HLOS.bin", "/dev/block/bootdevice/by-name/modem");')
    info.script.AppendExtra('package_extract_file("firmware-update/cmnlib.mbn", "/dev/block/bootdevice/by-name/cmnlib");')
    info.script.AppendExtra('package_extract_file("firmware-update/hyp.mbn", "/dev/block/bootdevice/by-name/hyp");')
    info.script.AppendExtra('package_extract_file("firmware-update/BTFM.bin", "/dev/block/bootdevice/by-name/bluetooth");')
    info.script.AppendExtra('package_extract_file("firmware-update/tz.mbn", "/dev/block/bootdevice/by-name/tz");')
    info.script.AppendExtra('package_extract_file("firmware-update/storsec.mbn", "/dev/block/bootdevice/by-name/storsec");')
    info.script.AppendExtra('package_extract_file("firmware-update/logfs_ufs_8mb.bin", "/dev/block/bootdevice/by-name/logfs");')
    info.script.AppendExtra('package_extract_file("firmware-update/abl.elf", "/dev/block/bootdevice/by-name/abl");')
    info.script.AppendExtra('package_extract_file("firmware-update/devcfg.mbn", "/dev/block/bootdevice/by-name/devcfg");')
    info.script.AppendExtra('package_extract_file("firmware-update/keymaster.mbn", "/dev/block/bootdevice/by-name/keymaster");')
    info.script.AppendExtra('package_extract_file("firmware-update/xbl.elf", "/dev/block/bootdevice/by-name/xbl");')
    info.script.AppendExtra('package_extract_file("firmware-update/rpm.mbn", "/dev/block/bootdevice/by-name/rpm");')
    info.script.AppendExtra('package_extract_file("firmware-update/cmnlib64.mbn", "/dev/block/bootdevice/by-name/cmnlib64bak");')
    info.script.AppendExtra('package_extract_file("firmware-update/cmnlib.mbn", "/dev/block/bootdevice/by-name/cmnlibbak");')
    info.script.AppendExtra('package_extract_file("firmware-update/hyp.mbn", "/dev/block/bootdevice/by-name/hypbak");')
    info.script.AppendExtra('package_extract_file("firmware-update/tz.mbn", "/dev/block/bootdevice/by-name/tzbak");')
    info.script.AppendExtra('package_extract_file("firmware-update/abl.elf", "/dev/block/bootdevice/by-name/ablbak");')
    info.script.AppendExtra('package_extract_file("firmware-update/devcfg.mbn", "/dev/block/bootdevice/by-name/devcfgbak");')
    info.script.AppendExtra('package_extract_file("firmware-update/keymaster.mbn", "/dev/block/bootdevice/by-name/keymasterbak");')
    info.script.AppendExtra('package_extract_file("firmware-update/xbl.elf", "/dev/block/bootdevice/by-name/xblbak");')
    info.script.AppendExtra('package_extract_file("firmware-update/rpm.mbn", "/dev/block/bootdevice/by-name/rpmbak");')
