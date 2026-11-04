# excerpt — https://developer.android.com/guide/topics/manifest/manifest-element (raw sha256 6e51f69c87a331bb94507a6ecf5a4e2487974cc1b9dfb1f7c00f7887078c7d2d; text = tags stripped, whitespace collapsed)

## M-root (offset 12841 in normalized text, 19 words)

```
e must contain: <application> can contain: <attribution> <compatible-screens> <instrumentation> <permission> <permission-group> <permission-tree> <queries> <supports-gl-texture> <supports-screens> <uses-configuration> <uses-feature> <uses-permission> <uses-permission-sdk-23> <uses-sdk> description: The root element of the AndroidManifest.xml file. It must contain an <application> element and specify xmlns:android and package attributes. attributes: xmlns:android Defines the Android namespace. This attribute is always set to "http://schemas.android.com/apk/res/android". package The value of the package attribute in the APK's manifest file represents your app's universally unique application ID. It is formatted as a full Java-langua
```

## M-ns (offset 13008 in normalized text, 11 words)

```
l-texture> <supports-screens> <uses-configuration> <uses-feature> <uses-permission> <uses-permission-sdk-23> <uses-sdk> description: The root element of the AndroidManifest.xml file. It must contain an <application> element and specify xmlns:android and package attributes. attributes: xmlns:android Defines the Android namespace. This attribute is always set to "http://schemas.android.com/apk/res/android". package The value of the package attribute in the APK's manifest file represents your app's universally unique application ID. It is formatted as a full Java-language-style package name for the Android app. The name can contain uppercase or lowercase letters, numbers, and underscores ('_'). However
```

## M-pkg (offset 13125 in normalized text, 18 words)

```
k> description: The root element of the AndroidManifest.xml file. It must contain an <application> element and specify xmlns:android and package attributes. attributes: xmlns:android Defines the Android namespace. This attribute is always set to "http://schemas.android.com/apk/res/android". package The value of the package attribute in the APK's manifest file represents your app's universally unique application ID. It is formatted as a full Java-language-style package name for the Android app. The name can contain uppercase or lowercase letters, numbers, and underscores ('_'). However, individual package name parts can only start with letters. Be careful not to change the package value, since that essentially
```

## M-vc (offset 17363 in normalized text, 19 words)

```
erId. If your app is newly installed on a device running an SDK version higher than the specified value, your app behaves as if you never defined android:sharedUserId. This attribute was introduced in API level 33. It is meaningful only if the sharedUserId attribute is also set. android:versionCode An internal version number. This number is used only to determine whether one version is more recent than another, with higher numbers indicating more recent versions. This isn't the version number shown to users, which is set by the versionName attribute. The value is set as a positive integer greater than 0. You can define it however you want, as long as each successive version has a higher number. For examp
```

## M-vn (offset 18040 in normalized text, 22 words)

```
rsion has a higher number. For example, it can be a build number, or you can translate a version number in "x.y" format to an integer by encoding the "x" and "y" separately in the lower and upper 16 bits. Or you can increase the number by one each time a new version is released. android:versionName The version number shown to users. This attribute is set as a raw string or as a reference to a string resource. The string has no other purpose than to display to users. The versionCode attribute holds the significant version number used internally. android:installLocation The default install location for the app. The following keyword strings are accepted: Value Description "internalOnly" The app installs o
```

## M-agp (offset 13693 in normalized text, 20 words)

```
erscores ('_'). However, individual package name parts can only start with letters. Be careful not to change the package value, since that essentially creates a new app. Users of the previous version of your app don't receive an update and can't transfer their data between the old and new versions. In the Gradle-based build system, starting with AGP 7.3, don't set the package value in the source manifest file directly. For more information, see Set the application ID. android:sharedUserId This constant is deprecated as of API level 29. Shared user IDs cause non-deterministic behavior within the package manager. As such, their use is strongly discouraged and might be removed in a future version of Android. Instead
```
