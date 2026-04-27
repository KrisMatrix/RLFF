use strict;
use warnings;

package PowerStation;
sub new {
    my ($class, $name, $output) = @_;
    my $self = { name => $name, output => $output };
    return bless $self, $class;
}

sub describe {
    my $self = shift;
    print "Station: $self->{name}, Output: $self->{output}MW\n";
}

package main;
my $plant = PowerStation->new("Millstone", 2100);
$plant->describe();