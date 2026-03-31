import pkg_resources

def packages_report():
    print("=== INSTALLED PYTHON PACKAGES ===")
    installed_packages = pkg_resources.working_set
    for package in sorted(installed_packages, key=lambda x: x.key):
        print(f"{package.key}=={package.version}")

if __name__ == "__main__":
    packages_report()
