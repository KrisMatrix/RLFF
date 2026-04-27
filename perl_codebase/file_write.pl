use strict;
use warnings;

my $filename = 'output_log.txt';

open(my $fh, '>', $filename) or die "Could not open file '$filename' $!";
print $fh "Log Entry: System Check Passed\n";
print $fh "Status: Operational\n";
close $fh;

print "Data written to $filename\n";