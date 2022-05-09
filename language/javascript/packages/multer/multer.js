const multer = require("multer");

const uploadPDF = multer({
  // This is the multer middleware
  dest: "images", // Destination folder
  limits: {
    fileSize: 5000000, // 1 MB
  },
  fileFilter(req, file, cb) {
    // cb(error,accepted/reject). E.g. cb(undefined, true)
    if (!file.originalname.match(/\.(doc|docx)$/)) {
      // Search can be customized with REGEX. E.g. /\.(doc|docx)$/         OR js functions !file.originalname.endsWith('.pdf')
      return cb(new Error("Please upload a PDF"));
    }

    cb(undefined, true); // If the file is OK.
  },
});

const errorMiddleware = (req, res, next) => {
  throw new Error("From my middleware");
};

app.post(
  "/task/upload",
  uploadPDF.single("upload"),
  (req, res) => {
    res.send();
  },
  (error, req, res, next) => {
    res.status(400).send({ error: error.message });
  }
);
