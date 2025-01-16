import os
import secrets


class EnvKeyGenerator:
    def __init__(self, env_file=".env"):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(script_dir)
        self.env_file = os.path.join(parent_dir, env_file)

    def generate_secret_key(self, length=50):
        return secrets.token_urlsafe(length)

    def update_env_key(self, key_name="APP_SECRET_KEY"):
        new_key = self.generate_secret_key()

        if not os.path.exists(self.env_file):
            raise FileNotFoundError(f"{self.env_file} does not exist.")

        with open(self.env_file, "r") as file:
            lines = file.readlines()

        key_found = False
        for i, line in enumerate(lines):
            if line.startswith(f"{key_name}="):
                lines[i] = f"{key_name}={new_key}\n"
                key_found = True
                break

        if not key_found:
            lines.append(f"{key_name}={new_key}\n")

        with open(self.env_file, "w") as file:
            file.writelines(lines)

        print(
            f"Generated {key_name} in {self.env_file} with a new value.\nkey: {new_key}"
        )


if __name__ == "__main__":
    env_generator = EnvKeyGenerator()
    try:
        env_generator.update_env_key()
    except FileNotFoundError as e:
        print(e)
