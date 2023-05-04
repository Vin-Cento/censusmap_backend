CREATE TABLE IF NOT EXISTS censustract (
  censuscode varchar(11) NOT NULL,
  statefp char(2) NOT NULL,
  countyfp char(3) NOT NULL,
  tractce char(6) NOT NULL,
  blkgrpce char(2) NOT NULL,
  affgeoid char(21) NOT NULL,
  geoid char(12) NOT NULL,
  lsad char(2) NOT NULL,
  aland bigint NOT NULL,
  awater bigint NOT NULL,
  state varchar(50),
  geometry geometry(geometry, 4269) NOT NULL,
  PRIMARY KEY (statefp, countyfp, tractce, blkgrpce)
);
