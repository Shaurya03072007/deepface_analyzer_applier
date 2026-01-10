
import sys
import traceback

print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")
print(f"sys.path: {sys.path}")

try:
    print("Attempting to import facefusion.processors.modules.face_swapper.core...")
    import facefusion.processors.modules.face_swapper.core
    print("Success: Module imported.")
except Exception:
    print("Failure: Could not import module.")
    traceback.print_exc()
