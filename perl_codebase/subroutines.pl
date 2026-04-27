use strict;
use warnings;

sub calculate_load {
    my ($base, $multiplier) = @_;
    return $base * $multiplier;
}

my $current_load = calculate_load(1500, 1.05);
print "Calculated Load: $current_load MW\n";