
# Query Criteria Reference

<!-- Auto-generated Markdown export of criteria tables -->

---

### Criteria on Basic Data

| Field    | Description                                                                                             | Operators                |
|----------|---------------------------------------------------------------------------------------------------------|--------------------------|
| pm       | proper motion (mas) as the Euclidean norm                                                               | `<`, `<=`, `>`, `>=`     |
| pmra     | right ascension of proper motion (mas)                                                                  | `<`, `<=`, `>`, `>=`     |
| pmdec    | declination of proper motion (mas)                                                                      | `<`, `<=`, `>`, `>=`     |
| pmqual   | proper motions quality (A:best, E:worst)                                                                | `=`, `!=`, `in`          |
| plx      | parallaxes (mas)                                                                                        | `=`, `!=`, `<`, `<=`, `>`, `>=` |
| plxqual  | parallax quality (A:best, E:worst)                                                                      | `=`, `!=`, `in`          |
| rvtype   | radial velocity type as entered in the database (`v`=radial velocity, `z`=redshift, `c`=cz velocity)    | `=`, `!=`                |
| radvel   | radial velocity (km/s)                                                                                  | `=`, `!=`, `<`, `<=`, `>`, `>=` |
| redshift | redshift                                                                                                | `=`, `!=`, `<`, `<=`, `>`, `>=` |
| vlsr     | vlsr                                                                                                    | `=`, `!=`, `<`, `<=`, `>`, `>=` |
| cz       | “cz” velocity                                                                                          | `=`, `!=`, `<`, `<=`, `>`, `>=` |
| rvqual   | radial velocity or redshift quality (A:best, E:worst)                                                   | `=`, `!=`, `in`          |
| sptype   | exact spectral type (e.g. `sptype='k0'` won’t return `K0III`)                                            | `=`, `!=`, `>`, `>=`, `<`, `<=`, `in` |
| sptypes  | all spectral types including sub‐types (e.g. `sptypes='k0'` returns `K0`, `K0III`, etc.)                 | `=`, `!=`, `>`, `>=`, `<`, `<=`, `in` |
| splum    | luminosity‐class only (`'III'`, `'IV/V'`, …)                                                            | `=`, `!=`, `>`, `>=`, `<`, `<=`, `in` |
| spqual   | spectral‐type quality (A:best, E:worst)                                                                  | `=`, `!=`, `in`          |
| spstring | spectral‐type string matching (e.g. `spstring~'M0'`)                                                     | `=`, `!=`, `~`, `!~`, `in` |
| mtype    | morphological type                                                                                     | `=`, `!=`, `~`, `!~`, `in` |
| mtqual   | morphological‐type quality (A:best, E:worst)                                                             | `=`, `!=`, `in`          |
| dimmajor | major axis of the dimension (arcmin)                                                                    | `=`, `!=`, `<`, `<=`, `>`, `>=` |
| dimminor | minor axis of the dimension (arcmin)                                                                    | `=`, `!=`, `<`, `<=`, `>`, `>=` |
| dimangle | angle of the major axis to the north pole (°?)                                                          | `=`, `!=`, `<`, `<=`, `>`, `>=` |
| dimqual  | dimension quality (A:best, E:worst)                                                                      | `=`, `!=`, `in`          |

---

### Criteria Based on Coordinates

| Field    | Description                                                                                                                                     | Operators            |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| region   | defines a sky region:  
`region(shape,frame,epoch,equinox,coords,dimension)`  
or  
`region(shape,identifier,dimension)`  
e.g. `region(CIRCLE,sirius,4m)`                                          | `none`               |
| ra       | right ascension (decimal degrees ≥ 0.0 and < 360.0)                                                                                              | `<`, `<=`, `>`, `>=` |
| rah      | right ascension (decimal hours ≥ 0.0 and < 24.0)                                                                                                 | `<`, `<=`, `>`, `>=` |
| dec      | declination (decimal degrees)                                                                                                                   | `<`, `<=`, `>`, `>=` |
| coobib   | coordinates bibcode                                                                                                                             | `=`, `!=`            |
| cooqual  | coordinates quality (A:best, E:worst)                                                                                                           | `=`, `!=`, `in`      |

---

### Magnitudes Available as Basic Data

| Field | Description          | Operators            |
|-------|----------------------|----------------------|
| Umag  | U magnitude          | `<`, `<=`, `>`, `>=` |
| Bmag  | B magnitude          | `<`, `<=`, `>`, `>=` |
| Vmag  | V magnitude          | `<`, `<=`, `>`, `>=` |
| Rmag  | R magnitude          | `<`, `<=`, `>`, `>=` |
| Imag  | I magnitude          | `<`, `<=`, `>`, `>=` |
| Gmag  | G (Gaia) magnitude   | `<`, `<=`, `>`, `>=` |
| Jmag  | J magnitude          | `<`, `<=`, `>`, `>=` |
| Kmag  | K magnitude          | `<`, `<=`, `>`, `>=` |
| Hmag  | H magnitude          | `<`, `<=`, `>`, `>=` |
| umag  | u (SDSS) magnitude   | `<`, `<=`, `>`, `>=` |
| gmag  | g (SDSS) magnitude   | `<`, `<=`, `>`, `>=` |
| rmag  | r (SDSS) magnitude   | `<`, `<=`, `>`, `>=` |
| imag  | i (SDSS) magnitude   | `<`, `<=`, `>`, `>=` |
| zmag  | z (SDSS) magnitude   | `<`, `<=`, `>`, `>=` |

---

### Object‐Type Criteria

| Field     | Description                                                                                                                | Operators       |
|-----------|----------------------------------------------------------------------------------------------------------------------------|-----------------|
| maintype  | query for a specific primary object type                                                                                  | `=`, `!=`, `in` |
| maintypes | query for the primary object to be included (sub‐category) in the given one                                               | `=>`, `in`, `!=`, `not in` |
| otype     | query for at least one secondary object type to appear                                                                     | `=`, `in`       |
| otypes    | query for at least one secondary subtype to be included                                                                    | `=>`, `in`      |

---

### Identifier & Measurement Availability

| Field | Description                                      | Operators                        |
|-------|--------------------------------------------------|----------------------------------|
| cat   | has an identifier in the given acronym(s)        | `=`, `!=`, `~`, `!~`, `in`       |
| mes   | has measurements in the given collection(s)      | `=`, `!=`, `~`, `!~`, `in`       |

---

### Criteria Based on Reference Data

| Field    | Description                                                                | Operators                         |
|----------|----------------------------------------------------------------------------|-----------------------------------|
| nbref    | total number of references for the object                                  | `=`, `!=`, `<`, `<=`, `>`, `>=`   |
| bibcode  | object cited in the reference                                              | `=`, `!=`, `in`                   |
| bibyear  | reference year (4-digit or range)                                          | `=`, `!=`, `<`, `<=`, `>`, `>=`   |
| journal  | journal abbreviation                                                        | `=`, `!=`, `~`, `!~`, `in`        |
| title    | string contained in the title                                              | `~`, `!~`                         |
| author   | reference author name                                                      | `=`, `~`                          |

---

### Criteria on Hierarchies

| Field      | Description                                                 | Operators                        |
|------------|-------------------------------------------------------------|----------------------------------|
| children   | query objects having the requested number of children       | `=`, `!=`, `>`, `>=`, `<`, `<=`  |
| parents    | query objects having the requested count of parents         | `=`, `!=`, `>`, `>=`, `<`, `<=`  |
| membership | probability flag between 0 and 100                          | `=`, `!=`, `>`, `>=`, `<`, `<=`  |
| hreference | the hierarchical link as the given reference                | `=`, `!=`, `in`                  |

---

## Criteria on Collection of Measurements

#### Diameter (stellar diameters)

| Field             | Description                                             | Operators                        |
|-------------------|---------------------------------------------------------|----------------------------------|
| Diameter.diameter | Diameter value linked to the unit                       | `=`, `!=`, `<`, `<=`, `>`, `>=`  |
| Diameter.unit     | Unit in which the diameter is defined (km)              | `=`, `!=`                       |
| Diameter.filter   | Filter used for computing the diameter (e.g. 'V')       | `=`, `!=`                       |
| Diameter.method   | Diameter calculation method (FundStP)                   | `=`, `!=`, `in`                  |
| Diameter.ref      | reference (bibcode) of the measurement                  | `=`, `!=`, `~`, `!~`             |

#### Distance (pc, kpc, Mpc by various methods)

| Field              | Description                                                                                         | Operators                        |
|--------------------|-----------------------------------------------------------------------------------------------------|----------------------------------|
| Distance.distance  | Distance value linked to the unit                                                                   | `=`, `!=`, `<`, `<=`, `>`, `>=`  |
| Distance.unit      | unit in which the distance is defined (`pc`, `kpc`, `Mpc`)                                          | `=`, `!=`                       |
| Distance.method    | method (`Cep`, `RRLYr`, `T-RGB`, `ST-L`, `T-F`, `redshift`, `SBF`, `kin`, `CalHK`)                | `=`, `!=`, `in`                  |
| Distance.ref       | reference (bibcode) of the measurement                                                              | `=`, `!=`, `~`, `!~`             |

#### Fe/H (Teff, log g, [Fe/H] metallicity)

| Field         | Description                                                   | Operators                        |
|---------------|---------------------------------------------------------------|----------------------------------|
| Fe_H.teff     | Effective Temperature (K)                                     | `=`, `!=`, `<`, `<=`, `>`, `>=`  |
| Fe_H.logg     | Decimal logarithm of the surface gravity                      | `=`, `!=`, `<`, `<=`, `>`, `>=`  |
| Fe_H.metidx   | Metallicity index relative to the Sun                         | `=`, `!=`, `<`, `<=`, `>`, `>=`  |
| Fe_H.flag     | Flag on the [Fe/H] value                                      | `=`, `!=`                       |
| Fe_H.compstar | comparison star from which the [Fe/H] value was obtained      | `=`, `!=`                       |
| Fe_H.ref      | reference (bibcode) of the measurement                        | `=`, `!=`, `~`, `!~`             |

#### SpT (spectral types)

| Field        | Description                                                 | Operators      |
|--------------|-------------------------------------------------------------|----------------|
| SpT.disp     | dispersive system (OP, PH, PO, P:prism, Sislit, G:grating)  | `=`, `!=`      |
| SpT.sptype   | MK/MSS spectral type                                        | `=`, `!=`, `~`, `!~` |
| SpT.mssNotes | mss notes                                                   | `=`, `!=`, `~`, `!~` |
| SpT.ref      | reference (bibcode) of the measurement                      | `=`, `!=`, `~`, `!~` |

#### Plx (trigonometric parallaxes)

| Field     | Description                                             | Operators                        |
|-----------|---------------------------------------------------------|----------------------------------|
| Plx.value | parallax (mas)                                          | `=`, `!=`, `<`, `<=`, `>`, `>=`  |
| Plx.obs   | Observatory code (A,C,D,G,L,Lo,M,Ma,S,Sd,St,U,V,W,Y,Yk) | `=`, `!=`                       |
| Plx.ref   | reference (bibcode) of the measurement                  | `=`, `!=`, `~`, `!~`             |

#### PM (proper motions)

| Field  | Description                             | Operators                        |
|--------|-----------------------------------------|----------------------------------|
| PM.ra  | Proper motion R.A. (arcsec)            | `=`, `!=`, `<`, `<=`, `>`, `>=`  |
| PM.dec | Proper motion Declination (arcsec)     | `=`, `!=`, `<`, `<=`, `>`, `>=`  |
| PM.ref | reference (bibcode) of the measurement | `=`, `!=`, `~`, `!~`             |

#### Rot (stellar rotational velocities)

| Field      | Description                          | Operators                        |
|------------|--------------------------------------|----------------------------------|
| Rot.vsini  | V sin i (km/s)                       | `=`, `!=`, `<`, `<=`, `>`, `>=`  |
| Rot.nbmess | Number of measurements               | `=`, `!=`, `<`, `<=`, `>`, `>=`  |
| Rot.qual   | Quality code (A…E)                   | `=`, `!=`, `<`, `<=`, `>`, `>=`  |
| Rot.ref    | reference (bibcode) of the measurement | `=`, `!=`, `~`, `!~`           |

#### Var (stellar variability types & periods)

| Field      | Description                                     | Operators                        |
|------------|-------------------------------------------------|----------------------------------|
| Var.type   | Type of variability                             | `=`, `!=`, `<`, `<=`, `>`, `>=`  |
| Var.period | Period                                          | `=`, `!=`, `<`, `<=`, `>`, `>=`  |
| Var.max    | Maximum of brightness                           | `=`, `!=`, `<`, `<=`, `>`, `>=`  |
| Var.rt     | Rising time for other variable types            | `=`, `!=`, `<`, `<=`, `>`, `>=`  |
| Var.min    | Minimum of brightness                           | `=`, `!=`, `<`, `<=`, `>`, `>=`  |
| Var.ref    | reference (bibcode) of the measurement          | `=`, `!=`, `~`, `!~`             |

#### Velocities (HRV, Vlsr, cz, redshifts)

| Field                     | Description                                         | Operators                        |
|---------------------------|-----------------------------------------------------|----------------------------------|
| Velocities.type           | velocity measurement type (`v`, `z`, `cz`)          | `=`, `!=`                       |
| Velocities.velocity       | velocity value by type                              | `=`, `!=`, `<`, `<=`, `>`, `>=`  |
| Velocities.nbmess         | number of measurements                              | `=`, `!=`, `<`, `<=`, `>`, `>=`  |
| Velocities.quality        | Quality of the measurement                          | `=`, `!=`                       |
| Velocities.wavelengthdomain| Wavelength domain (Rad, mm, IR, Opt, UV, XRay, Gam) | `=`, `!=`                       |
| Velocities.bibcode        | reference (bibcode) of the measurement              | `=`, `!=`                       |

---

### Criteria on Observing Logs

#### Herschel observing log

| Field           | Description                                                       | Operators                        |
|-----------------|-------------------------------------------------------------------|----------------------------------|
| Herschel.ObsId  | Observation identifier (quoted string)                            | `=`, `!=`                       |
| Herschel.alpha  | Right ascension (decimal degrees)                                 | `=`, `!=`, `<`, `<=`, `>`, `>=`  |
| Herschel.delta  | Declination (decimal degrees)                                     | `=`, `!=`, `<`, `<=`, `>`, `>=`  |
| Herschel.ref    | reference (bibcode) of the measurement                            | `=`, `!=`, `~`, `!~`             |

#### ISO observing log

| Field        | Description                                                       | Operators                        |
|--------------|-------------------------------------------------------------------|----------------------------------|
| ISO.tdt      | Observation identifier (quoted string)                            | `=`, `!=`                       |
| ISO.alpha    | Right ascension (decimal degrees)                                 | `=`, `!=`, `<`, `<=`, `>`, `>=`  |
| ISO.delta    | Declination (decimal degrees)                                     | `=`, `!=`, `<`, `<=`, `>`, `>=`  |
| ISO.ref      | reference (bibcode) of the measurement                            | `=`, `!=`, `~`, `!~`             |

#### IUE observing log

| Field                | Description                                  | Operators    |
|----------------------|----------------------------------------------|--------------|
| IUE.homogenized_name | Observation identifier                       | `=`, `!=`    |
| IUE.prog             | Observing Program identification             | `=`, `!=`    |
| IUE.ref              | reference (bibcode) of the measurement       | `=`, `!=`, `~`, `!~` |

#### XMM observing log

| Field     | Description                                | Operators        |
|-----------|--------------------------------------------|------------------|
| XMM.obs   | Observation identifier                     | `=`, `!=`        |
| XMM.ref   | reference (bibcode) of the measurement     | `=`, `!=`, `~`, `!~` |
