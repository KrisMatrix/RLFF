use strict;
use warnings;

my %bus_voltages = (
    "Bus1" => 115,
    "Bus2" => 345,
    "Bus3" => 230
);

print "The voltage at Bus2 is: " . $bus_voltages{"Bus2"} . "kV\n";