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
import os

TARGET_DIR = os.getenv('OUT_DIR')

# Firmware - sagit-firmware
def FullOTA_InstallEnd(info):
    info.output_zip.write(os.path.join(TARGET_DIR, "../device/xiaomi/sagit-firmware/firmware-update/abl.elf"), "firmware-update/abl.elf")
    info.output_zip.write(os.path.join(TARGET_DIR, "../device/xiaomi/sagit-firmware/firmware-update/BTFM.bin"), "firmware-update/BTFM.bin")
    info.output_zip.write(os.path.join(TARGET_DIR, "../device/xiaomi/sagit-firmware/firmware-update/cmnlib64.mbn"), "firmware-update/cmnlib64.mbn")
    info.output_zip.write(os.path.join(TARGET_DIR, "../device/xiaomi/sagit-firmware/firmware-update/cmnlib.mbn"), "firmware-update/cmnlib.mbn")
    info.output_zip.write(os.path.join(TARGET_DIR, "../device/xiaomi/sagit-firmware/firmware-update/devcfg.mbn"), "firmware-update/devcfg.mbn")
    info.output_zip.write(os.path.join(TARGET_DIR, "../device/xiaomi/sagit-firmware/firmware-update/hyp.mbn"), "firmware-update/hyp.mbn")
    info.output_zip.write(os.path.join(TARGET_DIR, "../device/xiaomi/sagit-firmware/firmware-update/keymaster.mbn"), "firmware-update/keymaster.mbn")
    info.output_zip.write(os.path.join(TARGET_DIR, "../device/xiaomi/sagit-firmware/firmware-update/logfs_ufs_8mb.bin"), "firmware-update/logfs_ufs_8mb.bin")
    info.output_zip.write(os.path.join(TARGET_DIR, "../device/xiaomi/sagit-firmware/firmware-update/NON-HLOS.bin"), "firmware-update/NON-HLOS.bin")
    info.output_zip.write(os.path.join(TARGET_DIR, "../device/xiaomi/sagit-firmware/firmware-update/rpm.mbn"), "firmware-update/rpm.mbn")
    info.output_zip.write(os.path.join(TARGET_DIR, "../device/xiaomi/sagit-firmware/firmware-update/storsec.mbn"), "firmware-update/storsec.mbn")
    info.output_zip.write(os.path.join(TARGET_DIR, "../device/xiaomi/sagit-firmware/firmware-update/tz.mbn"), "firmware-update/tz.mbn")
    info.output_zip.write(os.path.join(TARGET_DIR, "../device/xiaomi/sagit-firmware/firmware-update/xbl.elf"), "firmware-update/xbl.elf")

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
