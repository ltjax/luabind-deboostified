from cpt.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    # Cannot currently build shared since fPIC is not set correctly by the lua build
    builder.add_common_builds(shared_option_name=False)
    builder.run()
