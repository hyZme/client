// Generated by gencpp from file pcl_msgs/UpdateFilenameResponse.msg
// DO NOT EDIT!


#ifndef PCL_MSGS_MESSAGE_UPDATEFILENAMERESPONSE_H
#define PCL_MSGS_MESSAGE_UPDATEFILENAMERESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace pcl_msgs
{
template <class ContainerAllocator>
struct UpdateFilenameResponse_
{
  typedef UpdateFilenameResponse_<ContainerAllocator> Type;

  UpdateFilenameResponse_()
    : success(false)  {
    }
  UpdateFilenameResponse_(const ContainerAllocator& _alloc)
    : success(false)  {
  (void)_alloc;
    }



   typedef uint8_t _success_type;
  _success_type success;




  typedef boost::shared_ptr< ::pcl_msgs::UpdateFilenameResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pcl_msgs::UpdateFilenameResponse_<ContainerAllocator> const> ConstPtr;

}; // struct UpdateFilenameResponse_

typedef ::pcl_msgs::UpdateFilenameResponse_<std::allocator<void> > UpdateFilenameResponse;

typedef boost::shared_ptr< ::pcl_msgs::UpdateFilenameResponse > UpdateFilenameResponsePtr;
typedef boost::shared_ptr< ::pcl_msgs::UpdateFilenameResponse const> UpdateFilenameResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::pcl_msgs::UpdateFilenameResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::pcl_msgs::UpdateFilenameResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace pcl_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'pcl_msgs': ['/home/pi/catkin_ws_1/src/pcl_msgs/msg'], 'sensor_msgs': ['/opt/ros/kinetic/share/sensor_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::pcl_msgs::UpdateFilenameResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pcl_msgs::UpdateFilenameResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pcl_msgs::UpdateFilenameResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pcl_msgs::UpdateFilenameResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pcl_msgs::UpdateFilenameResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pcl_msgs::UpdateFilenameResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::pcl_msgs::UpdateFilenameResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "358e233cde0c8a8bcfea4ce193f8fc15";
  }

  static const char* value(const ::pcl_msgs::UpdateFilenameResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x358e233cde0c8a8bULL;
  static const uint64_t static_value2 = 0xcfea4ce193f8fc15ULL;
};

template<class ContainerAllocator>
struct DataType< ::pcl_msgs::UpdateFilenameResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "pcl_msgs/UpdateFilenameResponse";
  }

  static const char* value(const ::pcl_msgs::UpdateFilenameResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::pcl_msgs::UpdateFilenameResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool success\n\
\n\
";
  }

  static const char* value(const ::pcl_msgs::UpdateFilenameResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::pcl_msgs::UpdateFilenameResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.success);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct UpdateFilenameResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pcl_msgs::UpdateFilenameResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::pcl_msgs::UpdateFilenameResponse_<ContainerAllocator>& v)
  {
    s << indent << "success: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.success);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PCL_MSGS_MESSAGE_UPDATEFILENAMERESPONSE_H
