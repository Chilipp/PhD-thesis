# example call for generating a map
import psyplot.project as psy

maps = psy.plot.mapplot(
    'psy-maps-demo.nc',  # input file name, can also be data in memory
    name='t2m',          # variable to plot (can also be multiples
    ### formatoptions
    # colorbar label uses meta attributes of netCDF variable
    clabel='%(long_name)s [%(units)s]',
    # select colormap
    cmap='RdBu_r',
    # focus on a specific lonlatbox given by [lonmin, lonmax, latmin, latmax]
    lonlatbox=['Europe', 'Europe', 0, 'Europe'])

maps.show()