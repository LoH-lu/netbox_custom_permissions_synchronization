import logging
import traceback

from netbox.plugins import PluginTemplateExtension

logger = logging.getLogger(__name__)


class PrefixViewExtension(PluginTemplateExtension):
    models = ["ipam.prefix"]

    def buttons(self):
        try:
            obj = self.context.get("object")
            if not obj:
                return ""

            # Skip button for container prefixes
            if obj.status == "container":
                return ""

            return self.render(
                "netbox_custom_permissions_synchronization/sync_prefix_permissions_button.html",
                extra_context={"prefix": obj},
            )

        except Exception as e:
            logger.error(f"PrefixViewExtension.buttons(): {type(e).__name__}: {str(e)}")
            logger.error(traceback.format_exc())
            return ""


class VirtualMachineViewExtension(PluginTemplateExtension):
    models = ["virtualization.virtualmachine"]

    def buttons(self):
        try:
            obj = self.context.get("object")
            if not obj:
                return ""

            return self.render(
                "netbox_custom_permissions_synchronization/sync_vm_permissions_button.html",
                extra_context={"vm": obj},
            )

        except Exception as e:
            logger.error(f"VirtualMachineViewExtension.buttons(): {type(e).__name__}: {str(e)}")
            logger.error(traceback.format_exc())
            return ""


template_extensions = [PrefixViewExtension, VirtualMachineViewExtension]
