from gzip import open as gzip_open
from json import dump
from os.path import abspath, dirname, join

PROJECT_DIRECTORY_PATH = dirname(dirname(abspath(__file__)))

OUTPUT_DIRECTORY_PATH = join(PROJECT_DIRECTORY_PATH, 'output')


def count_variants():
    """
    Counted the number of variants in each chromosome and saved the results to
    ../output/output.json.
    Arguments:
        None
    Returns:
        None
    """

    with gzip_open(
            join(PROJECT_DIRECTORY_PATH, 'data', 'person',
                 'genome.vcf.gz')) as file_:

        chromosome_n_variant = {}

        current_chromosome = None

        for line in file_:

            line = line.decode()

            if not line.startswith('#'):

                chromosome = line.split('\t')[0]

                if current_chromosome is None or current_chromosome != chromosome:

                    current_chromosome = chromosome
                    chromosome_n_variant[current_chromosome] = 0

                else:
                    chromosome_n_variant[current_chromosome] += 1

    styled_chromosome_n_variant = {}

    for chromosome, n_variant in chromosome_n_variant.items():

        styled_chromosome_n_variant['Chromosome {}'.format(
            chromosome)] = '{} variants'.format(n_variant)

    output_json_file_path = join(OUTPUT_DIRECTORY_PATH, 'output.json')

    with open(output_json_file_path, 'w') as file_:
        dump(styled_chromosome_n_variant, file_, indent=2, sort_keys=True)

    print(
        'Counted the number of variants in each chromosome and saved the results to {}.'.
        format(output_json_file_path))


count_variants()
