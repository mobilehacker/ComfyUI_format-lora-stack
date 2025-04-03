import comfy.model_management

class FormatLoraStack:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"lora_stack": ("LORA_STACK",)} }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "format_loras"
    CATEGORY = "custom"

    def format_loras(self, lora_stack):
        if not lora_stack or not isinstance(lora_stack, list):
            return ("",)  # Return an empty string if no LoRAs are loaded
        
        formatted_loras = []
        for lora in lora_stack:
            if isinstance(lora, tuple) and len(lora) == 3:
                path, strength, _ = lora  # Extract filename and strength
                name = path.split("\\")[-1].replace(".safetensors", "")  # Get the file name without extension
                formatted_loras.append(f"<lora:{name}:{strength}>")
        
        return ("".join(formatted_loras),)

NODE_CLASS_MAPPINGS = {"FormatLoraStack": FormatLoraStack}
NODE_DISPLAY_NAME_MAPPINGS = {"FormatLoraStack": "Format LoRA Stack"}