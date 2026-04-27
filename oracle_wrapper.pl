use strict;
use warnings;
use JSON; 
use File::Spec;

# Define the source directory
my $subfolder = 'perl_codebase';

# List of your verified scripts
my @scripts = (
    'hello_world.pl', 'math_ops.pl', 'array_iteration.pl', 
    'subroutines.pl', 'file_write.pl', 'file_read.pl', 
    'conditionals.pl', 'hashes.pl', 'regex_parser.pl', 'oo_station.pl'
);

my %oracle_data;

foreach my $script_name (@scripts) {
    # Construct the full path: perl_codebase/script_name.pl
    my $path = File::Spec->catfile($subfolder, $script_name);

    if (-e $path) {
        # Execute script via the path and capture output
        my $output = `perl $path`;
        $oracle_data{$script_name} = {
            content => $output,
            timestamp => time()
        };
        print "Captured output for $path...\n";
    } else {
        warn "Warning: Could not find $path\n";
    }
}

# Save as ground_truth.json
my $output_file = 'ground_truth.json';
open(my $fh, '>', $output_file) or die "Could not open $output_file: $!";
print $fh encode_json(\%oracle_data);
close $fh;

print "\nSuccess: $output_file created from $subfolder.\n";