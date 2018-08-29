from followLogHander import FollowLogHander

logHandler = FollowLogHander()
logHandler.setInstName("niclasguenther")
logHandler.saveDataInDb()

peopleToUnfollow = logHandler.getData()
