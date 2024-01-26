import gzip
import shutil

def compress_file(input_filename, output_filename):
  with open(input_filename, 'rb') as f_in, gzip.open(output_filename, 'wb') as f_out:
    shutil.copyfileobj(f_in, f_out)

