# excerpt — https://developer.android.com/studio/publish/versioning (raw sha256 38314346d6db08b1919b866922254500d5bc0b4ac25aef7515d8bf621aa3f787; text = tags stripped, whitespace collapsed)

## V-vc (offset 13079 in normalized text, 9 words)

```
 namespace = "com.example.testapp" compileSdk = 33 defaultConfig { applicationId = "com.example.testapp" minSdk = 24 targetSdk = 33 versionCode = 1 versionName = "1.0" ... } ... } ... Version settings Define values for both of the version settings available: versionCode and versionName. versionCode A positive integer used as an internal version number. This number helps determine whether one version is more recent than another, with higher numbers indicating more recent versions. This is not the version number shown to users; that number is set by the versionName setting. The Android system uses the versionCode value to protect against downgrades
```

## V-vn (offset 14760 in normalized text, 10 words)

```
 with each release, regardless of whether the release constitutes a major or minor release. This means that the versionCode value doesn't necessarily resemble the app release version that is visible to the user. Apps and publishing services shouldn't display this version value to users. versionName A string used as the version number shown to users. This setting can be specified as a raw string or as a reference to a string resource. The value is a string so that you can describe the app version as a <major>.<minor>.<point> string or as any other type of absolute or relative version identifier. The versionName is the only value displayed to us
```
