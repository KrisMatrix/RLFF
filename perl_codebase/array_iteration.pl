use strict;
use warnings;

my @grid_zones = ("NEMA", "WCMA", "SEMA", "RI");

push(@grid_zones, "CT"); # Add to list

foreach my $zone (@grid_zones) {
    print "Processing Zone: $zone\n";
}