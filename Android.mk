LOCAL_PATH := $(call my-dir)

ifeq ($(TARGET_DEVICE),sagit)

include $(call all-makefiles-under,$(LOCAL_PATH))

endif
