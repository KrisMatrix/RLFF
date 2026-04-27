use strict;
use warnings;

my $filename = 'output_log.txt';

if (open(my $fh, '<', $filename)) {
    while (my $row = <$fh>) {
        chomp $row;
        print "Read from file: $row\n";
    }
    close $fh;
} else {
    warn "Could not read $filename. Does it exist yet?\n";
}