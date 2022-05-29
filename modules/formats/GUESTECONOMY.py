import logging
import struct

from modules.formats.BaseFormat import BaseFile


class GuestEconomyLoader(BaseFile):
    extension = ".guesteconomy"

    def create(self):
        # todo - fixme
        buffer_0 = self._get_data(self.file_entry.path)
        self.root_entry = self.create_root_entry(self.file_entry)
        self.write_data_to_pool(self.root_entry.struct_ptr, len(buffer_0), buffer_0)

    def collect(self):
        self.assign_root_entry()
        logging.debug(f"Collecting {self.root_entry.name}")
        self.root_entry.floats = []
        self.root_entry.floats = struct.unpack("<IfIfI27f", self.root_entry.struct_ptr.data)
        self.root_entry.guesteconomyrawdata = self.root_entry.struct_ptr.data
        logging.debug(f"data {self.root_entry.floats}")
        #TODO: instead of saving/loading it raw, finish the mapping and convert to xml?
        #data (500000, 0.0, 5000, 0.8500000238418579, 10000, 0.0, 0.0, 0.0, 750.0, 1000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 1.5, 0.4000000059604645, 1.0, 8.0, 4.0, 2.0, 2.0, 8.0, 200.0, 8.0, 0.0, 0.0, 0.0, 0.0)
        #GuestEconomy = {
        #    some parameters might be missing
        #    TargetTicketPrice = 180,
        #    TargetProfit = 500000,
        #    TargetDinosaurPrestige = 5000,
        #    TargetSpeciesVariety = 5,
        #    DinosaurPrestigePower = 0.65,
        #    TargetVisitors = 1000,
        #    VisitorArrivalRate = 750,
        #    VisitorDepartureRate = 1000,
        #    IncomeTaxMinIncome = 0,
        #    IncomeTaxMaxIncome = 0,
        #    IncomeTaxMinProportion = 0,
        #    IncomeTaxMaxProportion = 0,
        #    IncomeTaxCurvePower = 1,
        #    TicketPriceVisitorProportionPower = 0.75,
        #    TicketPriceFullVisitorProportion = 1.5,
        #    TicketPriceMinimumPriceFraction = 0.4,
        #    VisitorDeathsDecayRate = 2,
        #    VisitorDeathsLimit = 8,
        #    DangerExposureSafeDecayRate = 4,
        #    DangerExposureUnnecessaryShelterPunishment = 1.5,
        #    DangerExposureStormExposurePunishment = 6,
        #    DangerExposureDinosaurExposurePunishment = 8,
        #    DangerExposureDinosaurDangerRadius = 200,
        #    DangerExposureLimit = 8,
        #    TransportRatingDisabled = 0
        #},

    def extract(self, out_dir, show_temp_files, progress_callback):
        name = self.root_entry.name
        logging.info(f"Writing {name}")

        out_path = out_dir(name)
        data = self.root_entry.guesteconomyrawdata
        with open(out_path, 'wb') as outfile:
            outfile.write(data)
        return [out_path]

    def _get_data(self, file_path):
        """Loads raw data"""
        buffer_0 = self.get_content(file_path)
        return buffer_0