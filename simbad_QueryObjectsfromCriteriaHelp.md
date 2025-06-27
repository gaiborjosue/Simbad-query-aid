# SIMBAD: Query objects from criteria

Sampling is done by writing a combination of constraints pretty much like
the \itf where part of a SQL statement, but without having to know anything about
the structure of the database.

The available criteria are presented on the
web page, with the allowed
operators for each criteria.

This page contains detailed information on
particular topics.

Constraints

A single constraint has always the syntax:

criterion\_name  operator  value

The criterion name must be taken from the large list displayed on the
web page.

The operator must be one of the operators available for the criterion.
They are described below.

The value can be a numeric one (i.e. 12.35), a string enclosed in single quotes
(i.e. 'star') or a list of items enclosed in parenthesis, associated
with the 'IN' operator (i.e. ('hip','ppm'). If the items contain no spaces,
the quotes can be ommited for strings (i.e. (hip,ppm))

An exception to this syntax is made by the region criterion (see below)
which represents a constraint by itself, without operator, nor value.

Complex constraints can be build by combining single criterions with and
('&amp;') and or ('|') operators and parenthesis to group
sub-expressions.

Examples:

dec &gt; 85 &amp; (cat = 'hip' | cat = 'ppm') &amp; radvel &gt; 10

Get all objects having a declination over 85 deg, a radial velocity
over 10 km/sec and being in either the hipparcos or the ppm catalog.

region(GAL,180 0,2d) &amp; otype = 'G' &amp; (nbref &gt;= 10|bibyear &gt;= 2000)

Find all galaxies in a 2 deg radius circle around the anti galactic center
and having not less than 10 bibliographic references or references earlier
then 2000.

Operators

Each criterion – except the region criterion – can use
one or several operators Depending on a given criterion, These operators are:

|operator |  description |  example|
|=  |  equality |  otype = '*'|
|!=  |  not equal |  otype != 'galaxy'|
|&lt;  |  less than |  ubv.v &lt; 5.5|
|&lt;=  |  less or equal than |  sptype &lt;= 'G5'|
|&gt;  |  greater than |  pm &gt; 10|
|&gt;=  |  greater or equal than |  redshift &gt;= 1.0|
|∼|  contains the wildcard expression |  author ∼ 'egret*'|
|!∼|  does not contain the wildcard expression  ||
|in  |  contains at least one value among the list |  cat in ('hd','hip','ppm')|

Particular cases

Coordinate regions

This criterion defines a region in the sky. It can be combined with any other
criteria. Unlike others, it doesn't need an operator, nor a comparison value.

The region criterion has two syntaxes, and accepts many default
values, simplifying its writing:

region(shape, frame, epoch, equinox, coordinates, dimension, angle)

for querying by coordinates in any frame
region(shape, identifier, dimension, angle)

for querying around a given identifier

The different options are:

shape It defines the kind of region. The following shapes are available:

CIRCLE : A circle defined by the coordinates of the center and the radius
as dimension parameter. It is the default region type, and may be omitted.

Example: region(circle, gal, 123.5 -17.8, 0.5d)

ELLIPSE : An ellipse defined by the coordinates of the center and
the major and minor axes as the dimension parameter. The ellipse angle is the last
parameter.

Example: region(ellipse,12 30 +10 10,1d 0.5d,45)

ZONE : A zone is defined by two small circles (declination = constant)
and two great circles (right ascension = constant). The coordinates parameter
defines the center, and dimension defines the size in r.a. and decl.

Example : region(zone,10 30 +60 10, 3d 10m)

BOX : A box is defined by great circles in right ascension and declination.
The coordinates parameter defines the center, and dimension defines
the size in r.a. and decl.

Example : region(box,10 30 +60 10, 3d 10m)

ROTATEDBOX : Like a box. The rotation angle is a extra parameter after
the dimension parameter.

Example: region(rotatedbox,10 30 +60 10, 3d 10m,45)

POLYGON : A polygon defined by the coordinates of every node. No dimension
parameter is needed.

Example : region(polygon, gal,123 -10,124 -9,127 -12)

frame The coordinate frame is expressed by one of the following keywords:

ICRS,FK5,FK4,GAL,SGAL,ECL. The default is ICRS

epoch The coordinate epoch. If present, this parameter must be
prefixed by B or J. Epoch can be a decimal number (i.e. B1950.5, J2007.43).
The default is J2000.

equinox An equinox, needed for some frames (FK4). It is a decimal
number. The default is 2000.

coordinates They always contain a longitude and a latitude. The latitude
must be preceeded by a sign. They can be either given as decimal numbers, which
are always degrees or sexagesimal values, which represent by default hours for the
right ascension. For defining a POLYGON, coordinates are made of a comma
separated list of node coordinates, each of them contaiing a longitude and a latitude.

dimension Dimension are defined by one value for a circle, two values
for an ellipse, a zone, a box and a rotatedbox. By default the unit is arcmin. Arcsec,
arcmin or degrees can be explicitely specified by suffixing the radius by the letters
's', 'm' or 'd'. The default radius is 10m.

Example: 300s, 5m, 0.08333d

angle an ellipse and a rotatedbox require an angle parameter. It must be
expressed in degrees.

Example: 30, -45, 10.5

identifier a valid simbad identifier of an object having coordinates.
Its coordinates will be used as the center of the region. Frame, epoch and equinox used
are those of Simbad: ICRS,J2000,2000. This region definition cannot be used with a polygon.
An identifier must be surrounded with single quotes if it contains commas, otherwise the quotes
are optional.

Regions can also be combined using and (&amp;) and or (|) operators
and combined with other criteria:

(region(rotatedbox, gal, 120.10 -10.10, 5d 30m, 45)
| region(rotatedbox, gal, 120.10 -10.10, 5d 30m, -45))
&amp; Vmag &gt; 5.0

Proper motion

The pm criterion is done on the euclidian norm of pmra,pmdec.

pm = sqrt(pmra2+pmdec2)

Spectral types

A spectral types represent a complex data piece, and has therefore several
criteria:

sptype which is used to retrieve the objects having
exactly the requested type.

I.e. sptype = 'K0' will return only objects having 'K0' alone as spectral type.

sptypes which should be used to retrive all objects having a spectral
type containing the one specified.

I.e. sptypes = 'K0' will return all objects having 'K0' as a spectral type, but also 'K0III' or 'K0IIIp', ...).
splum can be used to retrieve objects having a given luminosity class.

I.e. splum = 'III', splum &gt;= 'IV'.

Equality operator does not include luminosity with uncertainty (':' suffix). To include
those in the query, it is needed to query

splum = 'II' | splum = 'II:' or

splum in ('II', 'II:').
sppec allows queries only by spectral type peculiarities.

I.e. sppec in ('cn','m').

Object types

Object types build a hierarchy defined here.

Each astronomical object has a main type defined, and several other types generally infered
from its identifiers.

Therefore, there are four different object type criterions:

maintype and otype looks for objects having exactly the requested type,
either as the main type or any type.

maintypes and otypes retrieves all objects having the given type or
any type underneath the given one in its hierarchy sub-tree.

Example:

otype = 'Pu*' retrieves all objects having exactly the generic type 'Pulsating variable star'.
otypes = 'Pu*' retrieves all objects having this type or any more specific type like
Mira Cet, RR Lyr, Cepheid, and so on..

Author names

Author names always contain the last name followed by the first name letters.
Queries are case insensitive.

One must be careful in the usage of the operators:

'=' (equal) means that the name you type must be exactly the one in the database:

author = 'egret d.' for instance will work, but not author = 'egret'.
∼ (tilde) means that the name you are searching will be appended by a '*'
as wildcard, if you don't write your own wildcards:

author ∼ 'jaschek' will return all objects having a reference with
JASCHEK C., JASCHEK M., JASCHEK-CORVALAN M. or JASCHEK C.O.
