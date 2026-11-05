package example;

/* metamodel_version: 1.12.0 */
/* version: 1.0, 1.1-rc3 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  How every entry of a group, or a single use of a component, gets its values: the fields, groups and components it sets.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraBlockAssignmentV11  {

  private List<OrchestraStructureMemberV11> fixrMembers;


}