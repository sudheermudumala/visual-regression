report({
  "testSuite": "BackstopJS",
  "tests": [
    {
      "pair": {
        "reference": "../bitmaps_reference/backstop_default_BackstopJS_Homepage_0_document_0_tablet.png",
        "test": "../bitmaps_test/20190201-103818/backstop_default_BackstopJS_Homepage_0_document_0_tablet.png",
        "selector": "document",
        "fileName": "backstop_default_BackstopJS_Homepage_0_document_0_tablet.png",
        "label": "BackstopJS Homepage",
        "requireSameDimensions": true,
        "misMatchThreshold": 0.1,
        "url": "https://weather.com/weather/today/l/USDC0001:1:US",
        "referenceUrl": "https://stage.weather.com/weather/today/l/USDC0001:1:US",
        "expect": 0,
        "viewportLabel": "tablet",
        "diff": {
          "isSameDimensions": false,
          "dimensionDifference": {
            "width": 0,
            "height": -30
          },
          "misMatchPercentage": "25.43",
          "analysisTime": 142
        },
        "diffImage": "../bitmaps_test/20190201-103818/failed_diff_backstop_default_BackstopJS_Homepage_0_document_0_tablet.png"
      },
      "status": "fail"
    }
  ],
  "id": "backstop_default"
});