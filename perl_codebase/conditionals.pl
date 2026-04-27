use strict;
use warnings;

my $threshold = 5000;
my $actual = 5200;

if ($actual > $threshold) {
    print "Warning: Threshold exceeded!\n";
} elsif ($actual == $threshold) {
    print "System at exact capacity.\n";
} else {
    print "Status: Normal.\n";
}