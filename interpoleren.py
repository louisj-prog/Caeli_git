import xarray as xr

# era5: columns idx_lon, idx_lat, idx_utc, + weather variables (e.g. temp, wind, etc.)
era5_sorted = era5.sort_values(["idx_utc", "idx_lat", "idx_lon"])

era5_ds = (
    era5_sorted
    .set_index(["idx_utc", "idx_lat", "idx_lon"])
    .to_xarray()
)

era5["idx_utc"] = pd.to_datetime(era5["idx_utc"])
modis["idx_utc"] = pd.to_datetime(modis["idx_utc"])

era5["idx_lon"] = era5["idx_lon"].round(2)
era5["idx_lat"] = era5["idx_lat"].round(2)

target_lon = xr.DataArray(modis["idx_lon"].values, dims="points")
target_lat = xr.DataArray(modis["idx_lat"].values, dims="points")
target_utc = xr.DataArray(modis["idx_utc"].values, dims="points")

interpolated = era5_ds.interp(
    idx_lon=target_lon,
    idx_lat=target_lat,
    idx_utc=target_utc,
    method="linear",
)

# Attach results back to modis
result = interpolated.to_dataframe().reset_index(drop=True)
modis_joined = pd.concat([modis.reset_index(drop=True), result], axis=1)
