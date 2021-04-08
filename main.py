from tools import validate_config_file, parse_config_file, fix_path, copy_files


def main(config_file):
    if not validate_config_file(config_file):
        return
    # get xml file tags
    file_tags = parse_config_file(config_file)

    for tag in file_tags:
        source_path = tag.attributes['source_path'].value
        file_path = fix_path(tag, source_path)
        destination_path = tag.attributes['destination_path'].value
        copy_files(file_path, destination_path)


if __name__ == "__main__":
    # insert your config file here
    main('conf_file')
