from owrx.source.connector import ConnectorSource, ConnectorDeviceDescription
from owrx.command import Flag, Option, Argument
from owrx.form.input import Input
from owrx.form.input.device import RemoteInput
from owrx.form.input.validator import Range
from typing import List


class GnuradioTcpSource(ConnectorSource):
    def getCommandMapper(self):
        return (
            super()
            .getCommandMapper()
            .setBase("gnuradio_tcp_connector")
            .setMappings(
                {
                    "remote": Argument(),
                }
            )
        )


class GnuradioTcpDeviceDescription(ConnectorDeviceDescription):
    def getName(self):
        return "GNURadio TCP Sink"

    def getInputs(self) -> List[Input]:
        return super().getInputs() + [RemoteInput()]

    def getDeviceMandatoryKeys(self):
        return super().getDeviceMandatoryKeys() + ["remote"]

    def getDeviceOptionalKeys(self):
        return super().getDeviceOptionalKeys()

    def getProfileOptionalKeys(self):
        return super().getProfileOptionalKeys()

    def getSampleRateRanges(self) -> List[Range]:
        return [Range(8000, 30000000)]
