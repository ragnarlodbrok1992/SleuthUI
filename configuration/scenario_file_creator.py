import configuration_default
import configuration_dict
from pprint import pprint
from collections import OrderedDict
import os


class ScenarioCreator(object):

    def __init__(self):
        self.self_path = __file__

        self.scenario_dict = OrderedDict

        self.main_comment = configuration_default.MAIN_COMMENT
        self.path_name_variables_comment = configuration_default.PATH_NAME_VARIABLES_COMMENT
        self.input_dir = configuration_default.INPUT_DIR
        self.output_dir = configuration_default.OUTPUT_DIR
        self.whirlgif_binary = configuration_default.WHIRLGIF_BINARY
        self.running_status_comment = configuration_default.RUNNING_STATUS_COMMENT
        self.echo = configuration_default.ECHO
        self.output_files_comment = configuration_default.OUTPUT_FILES_COMMENT
        self.write_coeff_file = configuration_default.WRITE_COEFF_FILE
        self.write_avg_file = configuration_default.WRITE_AVG_FILE
        self.write_std_dev_file = configuration_default.WRITE_STD_DEV_FILE
        self.write_memory_map = configuration_default.WRITE_MEMORY_MAP
        self.logging = configuration_default.LOGGING
        self.log_file_references_comment = configuration_default.LOG_FILE_PREFERENCES_COMMENT
        self.log_landclass_summary = configuration_default.LOG_LANDCLASS_SUMMARY
        self.log_slope_weights = configuration_default.LOG_SLOPE_WEIGHTS
        self.log_reads = configuration_default.LOG_READS
        self.log_writes = configuration_default.LOG_WRITES
        self.log_colortables = configuration_default.LOG_COLORTABLES
        self.log_processing_status = configuration_default.LOG_PROCESSING_STATUS
        self.log_transition_matrix = configuration_default.LOG_TRANSITION_MATRIX
        self.log_urbanization_attempts = configuration_default.LOG_URBANIZATION_ATTEMPTS
        self.log_initial_coefficients = configuration_default.LOG_INITIAL_COEFFICIENTS
        self.log_base_statistics = configuration_default.LOG_BASE_STATISTICS
        self.log_debug = configuration_default.LOG_DEBUG
        self.log_timings = configuration_default.LOG_TIMINGS
        self.working_grids_comment = configuration_default.WORKING_GRIDS_COMMENT
        self.num_working_grids = configuration_default.NUM_WORKING_GRIDS
        self.random_number_seed_comment = configuration_default.RANDOM_NUMBER_SEED_COMMENT
        self.random_seed = configuration_default.RANDOM_SEED
        self.monte_carlo_iterations_comment = configuration_default.MONTE_CARLO_ITERATIONS_COMMENT
        self.monte_carlo_iterations = configuration_default.MONTE_CARLO_ITERATIONS
        self.coefficients_comment = configuration_default.COEFFICIENTS_COMMENT

        self.calibration_diffusion_start = configuration_default.CALIBRATION_DIFFUSION_START
        self.calibration_diffusion_step = configuration_default.CALIBRATION_DIFFUSION_STEP
        self.calibration_diffusion_stop = configuration_default.CALIBRATION_DIFFUSION_STOP

        self.calibration_breed_start = configuration_default.CALIBRATION_BREED_START
        self.calibration_breed_step = configuration_default.CALIBRATION_BREED_STEP
        self.calibration_breed_stop = configuration_default.CALIBRATION_BREED_STOP

        self.calibration_spread_start = configuration_default.CALIBRATION_SPREAD_START
        self.calibration_spread_step = configuration_default.CALIBRATION_SPREAD_STEP
        self.calibration_spread_stop = configuration_default.CALIBRATION_SPREAD_STOP

        self.calibration_slope_start = configuration_default.CALIBRATION_SLOPE_START
        self.calibration_slope_step = configuration_default.CALIBRATION_SLOPE_STEP
        self.calibration_slope_stop = configuration_default.CALIBRATION_SLOPE_STOP

        self.calibration_road_start = configuration_default.CALIBRATION_ROAD_START
        self.calibration_road_step = configuration_default.CALIBRATION_ROAD_STEP
        self.calibration_road_stop = configuration_default.CALIBRATION_ROAD_STOP

        self.prediction_diffustion_best_fit = configuration_default.PREDICTION_DIFFUSION_BEST_FIT
        self.prediction_breed_best_fit = configuration_default.PREDICTION_BREED_BEST_FIT
        self.prediction_spread_best_fit = configuration_default.PREDICTION_SPREAD_BEST_FIT
        self.prediction_slope_best_fit = configuration_default.PREDICTION_SLOPE_BEST_FIT
        self.prediction_road_best_fit = configuration_default.PREDICTION_ROAD_BEST_FIT

        self.prediction_date_range_comment = configuration_default.PREDICTION_DATE_RANGE_COMMENT

        self.prediction_start_date = configuration_default.PREDICTION_START_DATE
        self.prediction_stop_date = configuration_default.PREDICTION_STOP_DATE

        self.input_images_comment = configuration_default.INPUT_IMAGES_COMMENT

        self.urban_data = configuration_default.URBAN_DATA
        self.road_data_comment = configuration_default.ROAD_DATA_COMMENT
        self.road_data = configuration_default.ROAD_DATA
        self.landuse_data_comment = configuration_default.LANDUSE_DATA_COMMENT
        self.landuse_data = configuration_default.LANDUSE_DATA
        self.excluded_data_comment = configuration_default.EXCLUDED_DATA_COMMENT
        self.excluded_data = configuration_default.EXCLUDED_DATA
        self.slope_data_comment = configuration_default.SLOPE_DATA_COMMENT
        self.slope_data = configuration_default.SLOPE_DATA
        self.background_data_comment = configuration_default.BACKGROUND_DATA_COMMENT
        self.background_data = configuration_default.BACKGROUND_DATA

        self.output_images_comment = configuration_default.OUTPUT_IMAGES_COMMENT
        self.write_color_key_images = configuration_default.WRITE_COLOR_KEY_IMAGES
        self.echo_images_files = configuration_default.ECHO_IMAGE_FILES
        self.animation = configuration_default.ANIMATION

        self.colortable_settings_comment = configuration_default.COLORTABLE_SETTINGS_COMMENT
        self.date_color = configuration_default.DATE_COLOR

        self.urban_non_landuse_colortable_settings = configuration_default.URBAN_NON_LANDUSE_COLORTABLE_SETTINGS
        self.seed_color = configuration_default.SEED_COLOR
        self.water_color_comment = configuration_default.WATER_COLOR_COMMENT
        self.water_color = configuration_default.WATER_COLOR

        self.probability_colortable_comment = configuration_default.PROBABILITY_COLORTABLE_COMMENT
        self.probaibility_color = configuration_default.PROBABILITY_COLOR

        self.land_cover_colortable_comment = configuration_default.LAND_COVER_COLORTABLE_COMMENT
        self.landuse_class = configuration_default.LANDUSE_CLASS
        self.growth_type_output_comment = configuration_default.GROWTH_TYPE_OUTPUT_COMMENT

        self.view_growth_types = configuration_default.VIEW_GROWTH_TYPES
        self.growth_type_print_window = configuration_default.GROWTH_TYPE_PRINT_WINDOW
        self.phase0g_growth_color = configuration_default.PHASE0G_GROWTH_COLOR
        self.phase1g_growth_color = configuration_default.PHASE1G_GROWTH_COLOR
        self.phase2g_growth_color = configuration_default.PHASE2G_GROWTH_COLOR
        self.phase3g_growth_color = configuration_default.PHASE3G_GROWTH_COLOR
        self.phase4g_growth_color = configuration_default.PHASE4G_GROWTH_COLOR
        self.phase5g_growth_color = configuration_default.PHASE5G_GROWTH_COLOR

        self.deltatron_aging_section = configuration_default.DELTATRON_AGING_SECTION

        self.view_deltatron_aging = configuration_default.VIEW_DELTATRON_AGING
        self.deltatron_print_window = configuration_default.DELTATRON_PRINT_WINDOW
        self.deltatron_color = configuration_default.DELTATRON_COLOR
        self.self_modification_comment = configuration_default.SELF_MODIFICATION_COMMENT

        self.road_grav_sensitivity = configuration_default.ROAD_GRAV_SENSITIVITY
        self.slope_sensitivity = configuration_default.SLOPE_SENSITIVITY
        self.critical_low = configuration_default.CRITICAL_LOW
        self.critical_high = configuration_default.CRITICAL_HIGH
        self.critical_slope = configuration_default.CRITICAL_SLOPE
        self.boom = configuration_default.BOOM
        self.bust = configuration_default.BUST

        self.configuration_dict = configuration_dict.CONF_VAR_DICT

    def print_all(self):
        pprint(vars(self))
        # for key, value in dict(vars(self)):
        #     print key, value

    def get_values(self):
        return vars(self)

    def save_to_file(self, path):

        file_string = str()

        file_string += self.main_comment
        file_string += self.path_name_variables_comment
        file_string += "INPUT_DIR=" + self.input_dir + "\n"
        file_string += "OUTPUT_DIR=" + self.output_dir + "\n"
        file_string += "WHIRLGIF_BINARY=" + self.whirlgif_binary + "\n"
        file_string += self.running_status_comment
        file_string += configuration_dict.CONF_VAR_DICT["ECHO"] + "=" + self.echo + "\n"
        file_string += self.output_files_comment

        file_string += configuration_dict.CONF_VAR_DICT["WRITE_COEFF_FILE"] + "=" + self.write_coeff_file + "\n"
        file_string += configuration_dict.CONF_VAR_DICT["WRITE_AVG_FILE"] + "=" + self.write_avg_file + "\n"
        file_string += configuration_dict.CONF_VAR_DICT["WRITE_STD_DEV_FILE"] + "=" + self.write_std_dev_file + "\n"
        file_string += configuration_dict.CONF_VAR_DICT["WRITE_MEMORY_MAP"] + "=" + self.write_memory_map + "\n"
        file_string += configuration_dict.CONF_VAR_DICT["LOGGING"] + "=" + self.logging + "\n"

        file_string += self.log_file_references_comment

        # Logging options
        file_string += configuration_dict.CONF_VAR_DICT["LOG_LANDCLASS_SUMMARY"] + "=" + self.log_landclass_summary + "\n"
        file_string += configuration_dict.CONF_VAR_DICT["LOG_SLOPE_WEIGHTS"] + "=" + self.log_slope_weights + "\n"
        file_string += configuration_dict.CONF_VAR_DICT["LOG_READS"] + "=" + self.log_reads + "\n"
        file_string += configuration_dict.CONF_VAR_DICT["LOG_WRITES"] + "=" + self.log_writes + "\n"
        file_string += configuration_dict.CONF_VAR_DICT["LOG_COLORTABLES"] + "=" + self.log_colortables + "\n"
        file_string += configuration_dict.CONF_VAR_DICT["LOG_PROCESSING_STATUS"] + "=" + str(self.log_processing_status) + "\n"
        file_string += configuration_dict.CONF_VAR_DICT["LOG_TRANSITION_MATRIX"] + "=" + self.log_transition_matrix + "\n"
        file_string += configuration_dict.CONF_VAR_DICT["LOG_URBANIZATION_ATTEMPTS"] + "=" + self.log_urbanization_attempts + "\n"
        file_string += configuration_dict.CONF_VAR_DICT["LOG_INITIAL_COEFFICIENTS"] + "=" + self.log_initial_coefficients + "\n"
        file_string += configuration_dict.CONF_VAR_DICT["LOG_BASE_STATISTICS"] + "=" + self.log_base_statistics + "\n"
        file_string += configuration_dict.CONF_VAR_DICT["LOG_DEBUG"] + "=" + self.log_debug + "\n"
        file_string += configuration_dict.CONF_VAR_DICT["LOG_TIMINGS"] + "=" + str(self.log_timings) + "\n"

        file_string += self.working_grids_comment
        file_string += "NUM_WORKING_GRIDS=" + str(self.num_working_grids) + "\n"

        file_string += self.random_number_seed_comment
        file_string += "RANDOM_SEED=" + str(self.random_seed) + "\n"

        file_string += self.monte_carlo_iterations_comment
        file_string += "MONTE_CARLO_ITERATIONS=" + str(self.monte_carlo_iterations) + "\n"

        file_string += self.coefficients_comment

        # Coefficients information
        file_string += "CALIBRATION_DIFFUSION_START=" + str(self.calibration_diffusion_start) + "\n"
        file_string += "CALIBRATION_DIFFUSION_STEP=" + str(self.calibration_diffusion_step) + "\n"
        file_string += "CALIBRATION_DIFFUSION_STOP=" + str(self.calibration_diffusion_stop) + "\n\n"

        file_string += "CALIBRATION_BREED_START=" + str(self.calibration_breed_start) + "\n"
        file_string += "CALIBRATION_BREED_STEP=" + str(self.calibration_breed_step) + "\n"
        file_string += "CALIBRATION_BREED_STOP=" + str(self.calibration_breed_stop) + "\n\n"

        file_string += "CALIBRATION_SPREAD_START=" + str(self.calibration_spread_start) + "\n"
        file_string += "CALIBRATION_SPREAD_STEP=" + str(self.calibration_spread_step) + "\n"
        file_string += "CALIBRATION_SPREAD_STOP=" + str(self.calibration_spread_stop) + "\n\n"

        file_string += "CALIBRATION_SLOPE_START=" + str(self.calibration_slope_start) + "\n"
        file_string += "CALIBRATION_SLOPE_STEP=" + str(self.calibration_slope_step) + "\n"
        file_string += "CALIBRATION_SLOPE_STOP=" + str(self.calibration_slope_stop) + "\n\n"

        file_string += "CALIBRATION_ROAD_START=" + str(self.calibration_road_start) + "\n"
        file_string += "CALIBRATION_ROAD_STEP=" + str(self.calibration_road_step) + "\n"
        file_string += "CALIBRATION_ROAD_STOP=" + str(self.calibration_road_stop) + "\n\n"

        # Best fit information
        file_string += "PREDICTION_DIFFUSION_BEST_FIT=" + str(self.prediction_diffustion_best_fit) + "\n"
        file_string += "PREDICTION_BREED_BEST_FIT=" + str(self.prediction_breed_best_fit) + "\n"
        file_string += "PREDICTION_SPREAD_BEST_FIT=" + str(self.prediction_spread_best_fit) + "\n"
        file_string += "PREDICTION_SLOPE_BEST_FIT=" + str(self.prediction_slope_best_fit) + "\n"
        file_string += "PREDICTION_ROAD_BEST_FIT=" + str(self.prediction_road_best_fit) + "\n\n"

        file_string += self.prediction_date_range_comment

        file_string += "PREDICTION_START_DATE=" + str(self.prediction_start_date) + "\n"
        file_string += "PREDICTION_STOP_DATE=" + str(self.prediction_stop_date) + "\n"

        file_string += self.input_images_comment

        for urb_data in self.urban_data:
            if urb_data is not "":
                file_string += "URBAN_DATA=" + urb_data + "\n"

        file_string += self.road_data_comment

        for rd_data in self.road_data:
            if rd_data is not "":
                file_string += "ROAD_DATA=" + rd_data + "\n"

        file_string += self.landuse_data_comment

        for lnd_data in self.landuse_data:
            if lnd_data is not "":
                file_string += "LANDUSE_DATA=" + lnd_data + "\n"

        file_string += self.excluded_data_comment

        for exl_data in self.excluded_data:
            if exl_data is not "":
                file_string += "EXCLUDED_DATA=" + exl_data + "\n"

        file_string += self.slope_data_comment

        for slp_data in self.slope_data:
            if slp_data is not "":
                file_string += "SLOPE_DATA=" + slp_data + "\n"

        file_string += self.background_data_comment

        for bkg_data in self.background_data:
            if bkg_data is not "":
                file_string += "BACKGROUND_DATA=" + bkg_data + "\n"

        file_string += self.output_images_comment

        file_string += configuration_dict.CONF_VAR_DICT["WRITE_COLOR_KEY_IMAGES"] + "=" + self.write_color_key_images + "\n"
        file_string += configuration_dict.CONF_VAR_DICT["ECHO_IMAGE_FILES"] + "=" + self.echo_images_files + "\n"
        file_string += configuration_dict.CONF_VAR_DICT["ANIMATION"] + "=" + self.animation + "\n"

        fd = os.open(path, os.O_RDWR|os.O_CREAT)
        ret = os.write(fd, file_string)
        return ret


if __name__ == "__main__":
    scr_creator = ScenarioCreator()
    # scr_creator.print_all()
    scr_creator.save_to_file(os.getcwd() + "\\" + "debug.txt")
    # print(os.getcwd())
    # print(os.getcwd() + "\debug.txt")
    # fd = os.open(os.getcwd() + "\\" + "debug.txt", os.O_RDWR|os.O_CREAT)
    # ret = os.write(fd, str(scr_creator.get_values()))
