MAIN_COMMENT = "# FILE: 'scenario file' for SLEUTH land cover transition model\n\
#       (UGM  v3.0)\n\
#       Comments start with #\n\
#\n\
#   I. Path Name Variables\n\
#  II. Running Status (Echo)\n\
# III. Output ASCII Files\n\
#  IV. Log File Preferences\n\
#   V. Working Grids\n\
#  VI. Random Number Seed\n\
# VII. Monte Carlo Iteration\n\
#VIII. Coefficients\n\
#      A. Coefficients and Growth Types\n\
#      B. Modes and Coefficient Settings\n\
#  IX. Prediction Date Range\n\
#   X. Input Images\n\
#  XI. Output Images\n\
# XII. Colortable Settings\n\
#      A. Date_Color\n\
#      B. Non-Landuse Colortable\n\
#      C. Land Cover Colortable\n\
#      D. Growth Type Images\n\
#      E. Deltatron Images\n\
#XIII. Self Modification Parameters\n"

PATH_NAME_VARIABLES_COMMENT = "# I.PATH NAME VARIABLES\n\
#   INPUT_DIR: relative or absolute path where input image files and\n\
#              (if modeling land cover) 'landuse.classes' file are\n\
#              located.\n\
#   OUTPUT_DIR: relative or absolute path where all output files will\n\
#               be located.\n\
#   WHIRLGIF_BINARY: relative path to 'whirlgif' gif animation program.\n\
#                    These must be compiled before execution.\n"
INPUT_DIR = "../Input/gdansk/"
OUTPUT_DIR = "../Output/gdansk_cal/"
WHIRLGIF_BINARY = "../Whirlgif/whirlgif"

RUNNING_STATUS_COMMENT = "# II. RUNNING STATUS (ECHO)\n\
#  Status of model run, monte carlo iteration, and year will be\n\
#  printed to the screen during model execution.\n"
ECHO = "yes"

OUTPUT_FILES_COMMENT = "# III. Output Files\n\
# INDICATE TYPES OF ASCII DATA FILES TO BE WRITTEN TO OUTPUT_DIRECTORY.\n\
#\n\
#   COEFF_FILE: contains coefficient values for every run, monte carlo\n\
#               iteration and year.\n\
#   AVG_FILE: contains measured values of simulated data averaged over\n\
#             monte carlo iterations for every run and control year.\n\
#   STD_DEV_FILE: contains standard diviation of averaged values\n\
#                 in the AVG_FILE.\n\
#   MEMORY_MAP: logs memory map to file 'memory.log'\n\
#   LOGGING: will create a 'LOG_#' file where # signifies the processor\n\
#            number that created the file if running code in parallel.\n\
#            Otherwise, # will be 0. Contents of the LOG file may be\n\
#            described below.\n"
WRITE_COEFF_FILE = "yes"
WRITE_AVG_FILE = "yes"
WRITE_STD_DEV_FILE = "yes"
WRITE_MEMORY_MAP = "YES"
LOGGING = "YES"

LOG_FILE_PREFERENCES_COMMENT = "# IV. Log File Preferences\n\
# INDICATE CONTENT OF LOG_# FILE (IF LOGGING == ON).\n\
#   LANDCLASS_SUMMARY: (if landuse is being modeled) summary of input\n\
#                      from 'landuse.classes' file\n\
#   SLOPE_WEIGHTS(YES/NO): annual slope weight values as effected\n\
#                          by slope_coeff\n\
#   READS(YES/NO)= notes if a file is read in\n\
#   WRITES(YES/NO)= notes if a file is written\n\
#   COLORTABLES(YES/NO)= rgb lookup tables for all colortables generated\n\
#   PROCESSING_STATUS(0:off/1:low verbosity/2:high verbosity)=\n\
#   TRANSITION_MATRIX(YES/NO)= pixel count and annual probability of\n\
#                              land class transitions\n\
#   URBANIZATION_ATTEMPTS(YES/NO)= number of times an attempt to urbanize\n\
#                                  a pixel occurred\n\
#   INITIAL_COEFFICIENTS(YES/NO)= initial coefficient values for\n\
#                                 each monte carlo\n\
#   BASE_STATISTICS(YES/NO)= measurements of urban control year data\n\
#   DEBUG(YES/NO)= data dump of igrid object and grid pointers\n\
#   TIMINGS(0:off/1:low verbosity/2:high verbosity)= time spent within\n\
#     each module. If running in parallel, LOG_0 will contain timing for\n\
#     complete job.\n"
LOG_LANDCLASS_SUMMARY = "yes"
LOG_SLOPE_WEIGHTS = "yes"
LOG_READS = "yes"
LOG_WRITES = "yes"
LOG_COLORTABLES = "yes"
LOG_PROCESSING_STATUS = 2
LOG_TRANSITION_MATRIX = "yes"
LOG_URBANIZATION_ATTEMPTS = "yes"
LOG_INITIAL_COEFFICIENTS = "yes"
LOG_BASE_STATISTICS = "yes"
LOG_DEBUG = "yes"
LOG_TIMINGS = 2

WORKING_GRIDS_COMMENT = "# V. WORKING GRIDS\n\
# The number of working grids needed from memory during model execution is\n\
\n\
# designated up front. This number may change depending upon modes. If\n\
# NUM_WORKING_GRIDS needs to be increased, the execution will be exited\n\
# and an error message will be written to the screen and to 'ERROR_LOG'\n\
# in the OUTPUT_DIRECTORY. If the number may be decreased an optimal\n\
# number will be written to the end of the LOG_0 file.\n"
NUM_WORKING_GRIDS = 8

RANDOM_NUMBER_SEED_COMMENT = "# VI. RANDOM NUMBER SEED\n\
# This number initializes the random number generator. This seed will be\n\
# used to initialize each model run.\n"
RANDOM_SEED = 1

MONTE_CARLO_ITERATIONS_COMMENT = "# VII. MONTE CARLO ITERATIONS\n\
# Each model run may be completed in a monte carlo fashion.\n\
#  For CALIBRATION or TEST mode measurements of simulated data will be\n\
#  taken for years of known data, and averaged over the number of monte\n\
#  carlo iterations. These averages are written to the AVG_FILE, and\n\
#  the associated standard diviation is written to the STD_DEV_FILE.\n\
#  The averaged values are compared to the known data, and a Pearson\n\
#  correlation coefficient measure is calculated and written to the\n\
#  control_stats.log file. The input per run may be associated across\n\
#  files using the 'index' number in the files' first column.\n\
#\n"
MONTE_CARLO_ITERATIONS = 10

COEFFICIENTS_COMMENT = "# VIII. COEFFICIENTS\n\
# The coefficients effect how the growth rules are applied to the data.\n\
# Setting requirements:\n\
#    *_START values >= *_STOP values\n\
#    *_STEP values > 0\n\
#   if no coefficient increment is desired:\n\
#    *_START == *_STOP\n\
#    *_STEP == 1\n\
# For additional information about how these values affect simulated\n\
# land cover change see our publications and PROJECT GIGALOPOLIS\n\
#  site: (www.ncgia.ucsb.edu/project/gig/About/abGrowth.htm).\n\
#  A. COEFFICIENTS AND GROWTH TYPES\n\
#     DIFFUSION: affects SPONTANEOUS GROWTH and search distance along the\n\
#                road network as part of ROAD INFLUENCED GROWTH.\n\
#     BREED: NEW SPREADING CENTER probability and affects number of ROAD\n\
#            INFLUENCED GROWTH attempts.\n\
#     SPREAD: the probabilty of ORGANIC GROWTH from established urban\n\
#             pixels occuring.\n\
#     SLOPE_RESISTANCE: affects the influence of slope to urbanization. As\n\
#                       value increases, the ability to urbanize\n\
#                       ever steepening slopes decreases.\n\
#     ROAD_GRAVITY: affects the outward distance from a selected pixel for\n\
#                   which a road pixel will be searched for as part of\n\
#                   ROAD INFLUENCED GROWTH.\n\
#\n\
#  B. MODES AND COEFFICIENT SETTINGS\n\
#     TEST: TEST mode will perform a single run through the historical\n\
#           data using the CALIBRATION_*_START values to initialize\n\
#           growth, complete the MONTE_CARLO_ITERATIONS, and then conclude\n\
#           execution. GIF images of the simulated urban growth will be\n\
#           written to the OUTPUT_DIRECTORY.\n\
#     CALIBRATE: CALIBRATE will perform monte carlo runs through the\n\
#                historical data using every combination of the\n\
#                coefficient values indicated. The CALIBRATION_*_START\n\
#                coefficient values will initialize the first run. A\n\
#                coefficient will then be increased by its *_STEP value,\n\
#                and another run performed. This will be repeated for all\n\
#                possible permutations of given ranges and increments.\n\
#     PREDICTION: PREDICTION will perform a single run, in monte carlo\n\
#                 fashion, using the PREDICTION_*_BEST_FIT values\n\
#                 for initialization.\n"

CALIBRATION_DIFFUSION_START = 1
CALIBRATION_DIFFUSION_STEP = 1
CALIBRATION_DIFFUSION_STOP = 6

CALIBRATION_BREED_START = 3
CALIBRATION_BREED_STEP = 1
CALIBRATION_BREED_STOP = 8

CALIBRATION_SPREAD_START = 28
CALIBRATION_SPREAD_STEP = 1
CALIBRATION_SPREAD_STOP = 33

CALIBRATION_SLOPE_START = 23
CALIBRATION_SLOPE_STEP = 1
CALIBRATION_SLOPE_STOP = 28

CALIBRATION_ROAD_START = 1
CALIBRATION_ROAD_STEP = 1
CALIBRATION_ROAD_STOP = 6

PREDICTION_DIFFUSION_BEST_FIT = 50
PREDICTION_BREED_BEST_FIT = 50
PREDICTION_SPREAD_BEST_FIT = 50
PREDICTION_SLOPE_BEST_FIT = 50
PREDICTION_ROAD_BEST_FIT = 50

PREDICTION_DATE_RANGE_COMMENT = "# IX. PREDICTION DATE RANGE\n\
# The urban and road images used to initialize growth during\n\
# prediction are those with dates equal to, or greater than,\n\
# the PREDICTION_START_DATE. If the PREDICTION_START_DATE is greater\n\
# than any of the urban dates, the last urban file on the list will be\n\
# used. Similarly, if the PREDICTION_START_DATE is greater\n\
# than any of the road dates, the last road file on the list will be\n\
# used. The prediction run will terminate at PREDICTION_STOP_DATE.\n\
#\n"
PREDICTION_START_DATE = 2003
PREDICTION_STOP_DATE = 2018

INPUT_IMAGES_COMMENT = "# X. INPUT IMAGES\n\
# The model expects grayscale, GIF image files with file name\n\
# format as described below. For more information see our\n\
# PROJECT GIGALOPOLIS web site:\n\
# (www.ncgia.ucsb.edu/project/gig/About/dtInput.htm).\n\
#\n\
# IF LAND COVER IS NOT BEING MODELED: Remove or comment out\n\
# the LANDUSE_DATA data input flags below.\n\
#\n\
#    <  >  = user selected fields\n\
#   [<  >] = optional fields\n\
#\n\
# Urban data GIFs\n\
#  format:  <location>.urban.<date>.[<user info>].gif\n\
#\n\
#\n"
URBAN_DATA = ["gdansk.urban.1880.gif",
              "gdansk.urban.1908.gif",
              "gdansk.urban.1930.gif",
              "gdansk.urban.1940.gif",
              "gdansk.urban.1959.gif",
              "gdansk.urban.1979.gif",
              "gdansk.urban.1985.gif",
              "gdansk.urban.2003.gif"]

ROAD_DATA_COMMENT = "#\n\
# Road data GIFs\n\
#  format:  <location>.roads.<date>.[<user info>].gif\n\
#\n"
ROAD_DATA = ["gdansk.roads.1940.gif",
             "gdansk.roads.1985.gif"]

LANDUSE_DATA_COMMENT = "#\n\
# Landuse data GIFs\n\
#  format:  <location>.landuse.<date>.[<user info>].gif\n\
#\n"
LANDUSE_DATA = [""]

EXCLUDED_DATA_COMMENT = "#\n\
# Excluded data GIF\n\
#  format:  <location>.excluded.[<user info>].gif\n\
#\n"
EXCLUDED_DATA = ["gdansk.excluded.gif"]

SLOPE_DATA_COMMENT = "#\n\
# Slope data GIF\n\
#  format:  <location>.slope.[<user info>].gif\n\
#\n"
SLOPE_DATA = ["gdansk.slope.gif"]

BACKGROUND_DATA_COMMENT = "#\n\
# Background data GIF\n\
#  format:   <location>.hillshade.[<user info>].gif\n\
#\n"
BACKGROUND_DATA = ["gdansk.hillshade.gif"]

OUTPUT_IMAGES_COMMENT = "# XI. OUTPUT IMAGES\n\
#   WRITE_COLOR_KEY_IMAGES: Creates image maps of each colortable.\n\
#                           File name format: 'key_[type]_COLORMAP'\n\
#                           where [type] represents the colortable.\n\
#   ECHO_IMAGE_FILES: Creates GIF of each input file used in that job.\n\
#                     File names format: 'echo_of_[input_filename]'\n\
#                     where [input_filename] represents the input name.\n\
#   ANIMATION: if whirlgif has been compiled, and the WHIRLGIF_BINARY\n\
#              path has been defined, animated gifs begining with the\n\
#              file name 'animated' will be created in PREDICT mode.\n"
WRITE_COLOR_KEY_IMAGES = "yes"
ECHO_IMAGE_FILES = "yes"
ANIMATION = "yes"

COLORTABLE_SETTINGS_COMMENT = "# XII. COLORTABLE SETTINGS\n\
#  A. DATE COLOR SETTING\n\
#     The date will automatically be placed in the lower left corner\n\
#     of output images. DATE_COLOR may be designated in with red, green,\n\
#     and blue values (format: <red_value, green_value, blue_value> )\n\
#     or with hexadecimal begining with '0X' (format: <0X######> ).\n\
#default DATE_COLOR= 0XFFFFFF white\n"
DATE_COLOR = 0XFFFFFF  # white

URBAN_NON_LANDUSE_COLORTABLE_SETTINGS = "#  B. URBAN (NON-LANDUSE) COLORTABLE SETTINGS\n\
#     1. URBAN MODE OUTPUTS\n\
#         TEST mode: Annual images of simulated urban growth will be\n\
#                    created using SEED_COLOR to indicate urbanized areas.\n\
\n\
#         CALIBRATE mode: Images will not be created.\n\
#         PREDICT mode: Annual probability images of simulated urban\n\
#                       growth will be created using the PROBABILITY\n\
#                       _COLORTABLE. The initializing urban data will be\n\
#                       indicated by SEED_COLOR.\n\
#\n\
#     2. COLORTABLE SETTINGS\n\
#          SEED_COLOR: initializing and extrapolated historic urban extent\n\
\n\
#          WATER_COLOR: BACKGROUND_DATA is used as a backdrop for\n\
\n\
#                       simulated urban growth. If pixels in this file\n\
#                       contain the value zero (0), they will be filled\n\
#                       with the color value in WATER_COLOR. In this way,\n\
#                       major water bodies in a study area may be included\n\
#                       in output images.\n\
#SEED_COLOR= 0XFFFF00 #yellow\n"
SEED_COLOR = [249, 209, 110]  # pale yellow
WATER_COLOR_COMMENT = "#WATER_COLOR=  0X0000FF # blue"
WATER_COLOR = [20, 52, 214]  # royal blue

PROBABILITY_COLORTABLE_COMMENT = "#     3. PROBABILITY COLORTABLE FOR URBAN GROWTH\n\
#        For PREDICTION, annual probability images of urban growth\n\
#        will be created using the monte carlo iterations. In these\n\
#        images, the higher the value the more likely urbanizaion is.\n\
#        In order to interpret these 'continuous' values more easily\n\
#        they may be color classified by range.\n\
#\n\
#        If 'hex' is not present then the range is transparent.\n\
#        The transparent range must be the first on the list.\n\
#        The max number of entries is 100.\n\
#          PROBABILITY_COLOR: a color value in hexadecimal that indicates\n\
#                             a probability range.\n\
#            low/upper: indicate the boundaries of the range.\n\
#\n\
#                  low,  upper,   hex,  (Optional Name)\n"
PROBABILITY_COLOR = [0,    1,  "0X000000",  # transparent
                     1,    10, "0X00ff33",  # green
                     10,   20, "0X00cc33",  #
                     20,   30, "0X009933",  #
                     30,   40, "0X006666",  # blue
                     40,   50, "0X003366",  #
                     50,   60, "0X000066",  #
                     60,   70, "0XFF6A6A",  # lt orange
                     70,   80, "0Xff7F00",  # dark orange
                     80,   90, "0Xff3E96",  # violetred
                     90,  100, "0Xff0033"]  # dark red

LAND_COVER_COLORTABLE_COMMENT = "#  C. LAND COVER COLORTABLE\n\
#  Land cover input images should be in grayscale GIF image format.\n\
#  The 'pix' value indicates a land class grayscale pixel value in\n\
#  the image. If desired, the model will create color classified\n\
#  land cover output. The output colortable is designated by the\n\
#  'hex/rgb' values.\n\
#    pix: input land class pixel value\n\
#    name: text string indicating land class\n\
#    flag: special case land classes\n\
#          URB - urban class (area is included in urban input data\n\
#                and will not be transitioned by deltatron)\n\
#          UNC - unclass (NODATA areas in image)\n\
#          EXC - excluded (land class will be ignored by deltatron)\n\
#    hex/rgb: hexidecimal or rgb (red, green, blue) output colors\n\
#\n\
#              pix, name,     flag,   hex/rgb, #comment\n"
LANDUSE_CLASS = [0,  "Unclass", "UNC", "0X000000",
                 1,  "Urban", "URB", "0X8b2323",  # dark red
                 2,  "Agric", "", "0Xffec8b",  # pale yellow
                 3,  "Range", "", "0Xee9a49",  # tan
                 4,  "Forest", "", "0X006400",
                 5,  "Water", "EXC", "0X104e8b",
                 6,  "Wetland", "", "0X483d8b",
                 7,  "Barren", "", "0Xeec591"]

GROWTH_TYPE_OUTPUT_COMMENT = "#  D. GROWTH TYPE IMAGE OUTPUT CONTROL AND COLORTABLE\n\
#\n\
#  From here you can control the output of the Z grid\n\
#  (urban growth) just after it is returned from the spr_spread()\n\
#  function. In this way it is possible to see the different types\n\
#  of growth that have occured for a particular growth cycle.\n\
#\n\
#  VIEW_GROWTH_TYPES(YES/NO) provides an on/off\n\
#  toggle to control whether the images are generated.\n\
#\n\
#  GROWTH_TYPE_PRINT_WINDOW provides a print window\n\
#  to control the amount of images created.\n\
#  format:  <start_run>,<end_run>,<start_monte_carlo>,\n\
#           <end_monte_carlo>,<start_year>,<end_year>\n\
#  for example:\n\
#  GROWTH_TYPE_PRINT_WINDOW=run1,run2,mc1,mc2,year1,year2\n\
#  so images are only created when\n\
#  run1<= current run <=run2 AND\n\
#  mc1 <= current monte carlo <= mc2 AND\n\
#  year1 <= currrent year <= year2\n\
#\n\
#  0 == first\n"
VIEW_GROWTH_TYPES = "YES"
GROWTH_TYPE_PRINT_WINDOW = 0, 0, 0, 0, 1995, 2020
PHASE0G_GROWTH_COLOR = "0xff0000"  # seed urban area
PHASE1G_GROWTH_COLOR = "0X00ff00"  # diffusion growth
PHASE2G_GROWTH_COLOR = "0X0000ff"  # NOT USED
PHASE3G_GROWTH_COLOR = "0Xffff00"  # breed growth
PHASE4G_GROWTH_COLOR = "0Xffffff"  # spread growth
PHASE5G_GROWTH_COLOR = "0X00ffff"  # road influenced growth

DELTATRON_AGING_SECTION = "#************************************************************\n\
#\n\
#  E. DELTATRON AGING SECTION\n\
#\n\
#  From here you can control the output of the deltatron grid\n\
#  just before they are aged\n\
#\n\
#  VIEW_DELTATRON_AGING(YES/NO) provides an on/off\n\
#  toggle to control whether the images are generated.\n\
#\n\
#  DELTATRON_PRINT_WINDOW provides a print window\n\
#  to control the amount of images created.\n\
#  format:  <start_run>,<end_run>,<start_monte_carlo>,\n\
#           <end_monte_carlo>,<start_year>,<end_year>\n\
#  for example:\n\
#  DELTATRON_PRINT_WINDOW=run1,run2,mc1,mc2,year1,year2\n\
#  so images are only created when\n\
#  run1<= current run <=run2 AND\n\
#  mc1 <= current monte carlo <= mc2 AND\n\
#  year1 <= currrent year <= year2\n\
#\n\
#  0 == first\n"
VIEW_DELTATRON_AGING = "YES"
DELTATRON_PRINT_WINDOW = 0, 0, 0, 0, 1930, 2020
DELTATRON_COLOR = ["0x000000",  # index 0 No or dead deltatron
                   "0X00FF00",  # index 1 age = 1 year
                   "0X00D200",  # index 2 age = 2 year
                   "0X00AA00",  # index 3 age = 3 year
                   "0X008200",  # index 4 age = 4 year
                   "0X005A00"]  # index 5 age = 5 year

SELF_MODIFICATION_COMMENT = "# XIII. SELF-MODIFICATION PARAMETERS\n\
#       SLEUTH is a self-modifying cellular automata. For more\n\
#       information see our PROJECT GIGALOPOLIS web site\n\
#       (www.ncgia.ucsb.edu/project/gig/About/abGrowth.htm)\n\
#       and publications (and/or grep 'self modification' in code).\n"
ROAD_GRAV_SENSITIVITY = 0.01
SLOPE_SENSITIVITY = 0.1
CRITICAL_LOW = 0.97
CRITICAL_HIGH = 1.3
# CRITICAL_LOW=0.0
# CRITICAL_HIGH=10000000000000.0
CRITICAL_SLOPE = 15.0
BOOM = 1.01
BUST = 0.09
