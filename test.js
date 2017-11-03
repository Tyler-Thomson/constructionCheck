let mongoose = require('mongoose');
let User = mongoose.model('User');
let ip_collect = require('./mac_collect');


module.exports = {
  index: function(req, res){
    User.find({}, (err, users) =>{
      if(err){return res.json(err)}
      return res.json(users);
    })
  },
  create: function(req, res){
    let mac_address = ip_collect.collect_one_mac(req.connection.localAddress);
    User.findOne({email: req.body.email}, (err, user) => {
      if(err){return res.json(err)}
      else if(!user){
        User.create(req.body, (err, user) => {
          if(err){return res.json(err)}
          user.mac_address = mac_address;
          user.save();
          return res.json(user);
        });
        // If user is found, retrieve and save mac address (if not already saved)
      }else{
        if(!(mac_address in user.mac_address)){
          user.mac_address.push(mac_address)
        }
        return res.json(user);
      }
    })
  },
  show: function(req, res){
    User.findById(req.params.id, function(err, user){
      if(!user){return res.json({error:'Invalid user ID'})}
      if(err){return res.json(err)}
      return res.json(user);
    })
  },
  update: function(req, res){
		User.findByIdAndUpdate(req.params.id, { $set: req.body }, function(err, user){
			if(err){return res.json(err)}
      else{return res.json(user)}
     })
  },
  destroy: function(req, res){
    User.findByIdAndRemove(req.params.id, function(err, user){
      if(err){return res.json(err)}
	     return res.json(user);
    })
  },
  scan: function(req, res){
    User.find({}, (err, users) =>{
      if(err){return res.json(err)}
      let all_macs = ip_collect.collect_all_macs().split("\n");
      let current_hour = (new Date()).getHours().toString();
      for(let user of users){
        for(let mac of user.mac_address){
          if(mac in all_macs){
            user.attendance[current_hour] = true;
            user.save();
          }
        }
      }
      return res.json(users);
    })
  }
}
