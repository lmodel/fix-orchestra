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
  A block whose entries repeat, each with the same fields, components and groups, and whose count a NumInGroup field carries.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraGroupV10  {

  private OrchestraFieldRefV10 fixrNumInGroup;
  private List<OrchestraStructureMemberV10> fixrMembers;
  private OrchestraAnnotationV10 fixrAnnotation;
  private String fixrCategory;
  private String fixrRendering;
  private Integer fixrImplMinOccurs;
  private String fixrImplMaxOccurs;
  private String fixrWhich;
  private String fixrAdded;
  private Integer fixrAddedEp;
  private String fixrChangeType;
  private String fixrDeprecated;
  private Integer fixrDeprecatedEp;
  private String fixrIssue;
  private String fixrLastModified;
  private String fixrReplaced;
  private Integer fixrReplacedEp;
  private Integer fixrReplacedByField;
  private String fixrSupported;
  private String fixrUpdated;
  private Integer fixrUpdatedEp;
  private int fixrId;
  private String fixrName;
  private String fixrAbbrName;
  private String fixrScenario;


}