use strict;
use warnings;

my $log_line = "ERROR_CODE: 404 at 12:00PM";

if ($log_line =~ /ERROR_CODE: (\d+)/) {
    print "Extracted Error ID: $1\n";
}

$log_line =~ s/404/500/; # Replace 404 with 500
print "Corrected Line: $log_line\n";