# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ComOption(models.Model):
    action = models.CharField(db_column='ACTION', max_length=15, blank=True, null=True)  # Field name made lowercase.
    taxonomy = models.CharField(db_column='TAXONOMY', primary_key=True, max_length=70)  # Field name made lowercase.
    execution_timestamp = models.CharField(db_column='EXECUTION_TIMESTAMP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    option_type = models.CharField(db_column='OPTION_TYPE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    underlying_asset_1 = models.CharField(db_column='UNDERLYING_ASSET_1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    underlying_asset_2 = models.CharField(db_column='UNDERLYING_ASSET_2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    effective_date = models.CharField(db_column='EFFECTIVE_DATE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    end_date = models.CharField(db_column='END_DATE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    rounded_notional_amount_1 = models.CharField(db_column='ROUNDED_NOTIONAL_AMOUNT_1', max_length=15, blank=True, null=True)  # Field name made lowercase.
    notional_currency_1 = models.CharField(db_column='NOTIONAL_CURRENCY_1', max_length=8, blank=True, null=True)  # Field name made lowercase.
    cleared = models.CharField(db_column='CLEARED', max_length=5, blank=True, null=True)  # Field name made lowercase.
    option_strike_price = models.CharField(db_column='OPTION_STRIKE_PRICE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    price_notation_type = models.CharField(db_column='PRICE_NOTATION_TYPE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    option_premium = models.CharField(db_column='OPTION_PREMIUM', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COM/OPTION'


class ComSwap(models.Model):
    action = models.CharField(db_column='ACTION', max_length=15, blank=True, null=True)  # Field name made lowercase.
    taxonomy = models.CharField(db_column='TAXONOMY', primary_key=True, max_length=70)  # Field name made lowercase.
    execution_timestamp = models.CharField(db_column='EXECUTION_TIMESTAMP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    underlying_asset_1 = models.CharField(db_column='UNDERLYING_ASSET_1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    underlying_asset_2 = models.CharField(db_column='UNDERLYING_ASSET_2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    end_date = models.CharField(db_column='END_DATE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    rounded_notional_amount_1 = models.CharField(db_column='ROUNDED_NOTIONAL_AMOUNT_1', max_length=15, blank=True, null=True)  # Field name made lowercase.
    notional_currency_1 = models.CharField(db_column='NOTIONAL_CURRENCY_1', max_length=8, blank=True, null=True)  # Field name made lowercase.
    payment_frequency_1 = models.CharField(db_column='PAYMENT_FREQUENCY_1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cleared = models.CharField(db_column='CLEARED', max_length=5, blank=True, null=True)  # Field name made lowercase.
    price_notation = models.CharField(db_column='PRICE_NOTATION', max_length=15, blank=True, null=True)  # Field name made lowercase.
    price_notation_type = models.CharField(db_column='PRICE_NOTATION_TYPE', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COM/SWAP'


class FredBase(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/BASE'


class FredCivpart(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/CIVPART'


class FredCp(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/CP'


class FredCpiaucsl(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/CPIAUCSL'


class FredCpilfesl(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/CPILFESL'


class FredDcoilwtico(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/DCOILWTICO'


class FredDff(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/DFF'


class FredDgs10(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/DGS10'


class FredDgs30(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/DGS30'


class FredDgs5(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/DGS5'


class FredDprime(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/DPRIME'


class FredDspi(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/DSPI'


class FredDspic96(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/DSPIC96'


class FredDtb3(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/DTB3'


class FredDtwexb(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/DTWEXB'


class FredDtwexm(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/DTWEXM'


class FredEmratio(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/EMRATIO'


class FredExcsresnw(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/EXCSRESNW'


class FredGdp(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/GDP'


class FredGdpc1(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/GDPC1'


class FredGdpdef(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/GDPDEF'


class FredGdppot(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/GDPPOT'


class FredGfdebtn(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/GFDEBTN'


class FredGfdegdq188S(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/GFDEGDQ188S'


class FredGpdi(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/GPDI'


class FredHoust(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/HOUST'


class FredIc4Wsa(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/IC4WSA'


class FredIcsa(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/ICSA'


class FredIndpro(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/INDPRO'


class FredM1(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/M1'


class FredM1V(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/M1V'


class FredM2(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/M2'


class FredM2V(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/M2V'


class FredManemp(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/MANEMP'


class FredMehoinusa672N(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/MEHOINUSA672N'


class FredNrou(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/NROU'


class FredNroust(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/NROUST'


class FredPayems(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/PAYEMS'


class FredPce(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/PCE'


class FredPcedg(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/PCEDG'


class FredPsavert(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/PSAVERT'


class FredRrsfs(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/RRSFS'


class FredStlfsi(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/STLFSI'


class FredT10Yie(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/T10YIE'


class FredT5Yie(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/T5YIE'


class FredT5Yifr(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/T5YIFR'


class FredTcu(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/TCU'


class FredTedrate(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/TEDRATE'


class FredTotci(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/TOTCI'


class FredUnemploy(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/UNEMPLOY'


class FredUnrate(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/UNRATE'


class FredUsslind(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRED/USSLIND'


class NewestDate(models.Model):
    name = models.CharField(db_column='NAME', primary_key=True, max_length=20)  # Field name made lowercase.
    date = models.CharField(db_column='DATE', max_length=18, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NEWEST_DATE'


class Dtcc(models.Model):
    dissemination_id = models.IntegerField(db_column='DISSEMINATION_ID', primary_key=True)  # Field name made lowercase.
    original_dissemination_id = models.IntegerField(db_column='ORIGINAL_DISSEMINATION_ID', blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='ACTION', max_length=15, blank=True, null=True)  # Field name made lowercase.
    execution_timestamp = models.CharField(db_column='EXECUTION_TIMESTAMP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cleared = models.CharField(db_column='CLEARED', max_length=5, blank=True, null=True)  # Field name made lowercase.
    indication_of_collateralization = models.CharField(db_column='INDICATION_OF_COLLATERALIZATION', max_length=2, blank=True, null=True)  # Field name made lowercase.
    indication_of_end_user_exception = models.CharField(db_column='INDICATION_OF_END_USER_EXCEPTION', max_length=1, blank=True, null=True)  # Field name made lowercase.
    indication_of_other_price_affecting_term = models.CharField(db_column='INDICATION_OF_OTHER_PRICE_AFFECTING_TERM', max_length=1, blank=True, null=True)  # Field name made lowercase.
    block_trades_and_large_notional_off_facility_swaps = models.CharField(db_column='BLOCK_TRADES_AND_LARGE_NOTIONAL_OFF-FACILITY_SWAPS', max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    execution_venue = models.CharField(db_column='EXECUTION_VENUE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    effective_date = models.CharField(db_column='EFFECTIVE_DATE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    end_date = models.CharField(db_column='END_DATE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    day_count_convention = models.CharField(db_column='DAY_COUNT_CONVENTION', max_length=20, blank=True, null=True)  # Field name made lowercase.
    settlement_currency = models.CharField(db_column='SETTLEMENT_CURRENCY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    asset_class = models.CharField(db_column='ASSET_CLASS', max_length=5, blank=True, null=True)  # Field name made lowercase.
    sub_asset_class_for_other_commodity = models.CharField(db_column='SUB-ASSET_CLASS_FOR_OTHER_COMMODITY', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    taxonomy = models.CharField(db_column='TAXONOMY', max_length=70, blank=True, null=True)  # Field name made lowercase.
    price_forming_continuation_data = models.CharField(db_column='PRICE_FORMING_CONTINUATION_DATA', max_length=15, blank=True, null=True)  # Field name made lowercase.
    underlying_asset_1 = models.CharField(db_column='UNDERLYING_ASSET_1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    underlying_asset_2 = models.CharField(db_column='UNDERLYING_ASSET_2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    price_notation_type = models.CharField(db_column='PRICE_NOTATION_TYPE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    price_notation = models.CharField(db_column='PRICE_NOTATION', max_length=15, blank=True, null=True)  # Field name made lowercase.
    additional_price_notation_type = models.CharField(db_column='ADDITIONAL_PRICE_NOTATION_TYPE', max_length=8, blank=True, null=True)  # Field name made lowercase.
    additional_price_notation = models.CharField(db_column='ADDITIONAL_PRICE_NOTATION', max_length=15, blank=True, null=True)  # Field name made lowercase.
    notional_currency_1 = models.CharField(db_column='NOTIONAL_CURRENCY_1', max_length=8, blank=True, null=True)  # Field name made lowercase.
    notional_currency_2 = models.CharField(db_column='NOTIONAL_CURRENCY_2', max_length=8, blank=True, null=True)  # Field name made lowercase.
    rounded_notional_amount_1 = models.CharField(db_column='ROUNDED_NOTIONAL_AMOUNT_1', max_length=15, blank=True, null=True)  # Field name made lowercase.
    rounded_notional_amount_2 = models.CharField(db_column='ROUNDED_NOTIONAL_AMOUNT_2', max_length=15, blank=True, null=True)  # Field name made lowercase.
    payment_frequency_1 = models.CharField(db_column='PAYMENT_FREQUENCY_1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    payment_frequency_2 = models.CharField(db_column='PAYMENT_FREQUENCY_2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reset_frequency_1 = models.CharField(db_column='RESET_FREQUENCY_1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reset_frequency_2 = models.CharField(db_column='RESET_FREQUENCY_2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    embeded_option = models.CharField(db_column='EMBEDED_OPTION', max_length=10, blank=True, null=True)  # Field name made lowercase.
    option_strike_price = models.CharField(db_column='OPTION_STRIKE_PRICE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    option_type = models.CharField(db_column='OPTION_TYPE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    option_family = models.CharField(db_column='OPTION_FAMILY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    option_currency = models.CharField(db_column='OPTION_CURRENCY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    option_premium = models.CharField(db_column='OPTION_PREMIUM', max_length=15, blank=True, null=True)  # Field name made lowercase.
    option_lock_period = models.CharField(db_column='OPTION_LOCK_PERIOD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    option_expiration_date = models.CharField(db_column='OPTION_EXPIRATION_DATE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    price_notation2_type = models.CharField(db_column='PRICE_NOTATION2_TYPE', max_length=8, blank=True, null=True)  # Field name made lowercase.
    price_notation2 = models.CharField(db_column='PRICE_NOTATION2', max_length=12, blank=True, null=True)  # Field name made lowercase.
    price_notation3_type = models.CharField(db_column='PRICE_NOTATION3_TYPE', max_length=8, blank=True, null=True)  # Field name made lowercase.
    price_notation3 = models.CharField(db_column='PRICE_NOTATION3', max_length=12, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dtcc'
