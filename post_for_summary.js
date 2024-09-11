async function getSummary(api, activeTabUrl) {
  try {
    const response = await fetch(api, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        video_url: activeTabUrl,
      }),
    });
    const responseData = await response.text(); 
  
    var progressCircle = document.getElementById("progress");

    progressCircle.style.visibility = "hidden";

    progressCircle.style.display = "none";

    let summary = document.getElementById("content");

    if(response.status === 200){
      summary.innerHTML = responseData;
    }else{
      let s
      summary.style.color = "#FF0000"
      summary.style.textAlign = 'center'
      summary.innerHTML = "Transcript Not Found";
    }

  } catch (error) {
    console.error("Error:", error);
  }
}

export { getSummary };
